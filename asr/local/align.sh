#:!/bin/bash
. ./cmd.sh
. ./path.sh

cd $root/asr

data=test

## Extract MFCCs
mfccdir=mfcc
steps/make_mfcc.sh --cmd "$train_cmd" --nj 1 data/$data exp/make_mfcc/$data $mfccdir || exit 1;
steps/compute_cmvn_stats.sh data/$data exp/make_mfcc/$data $mfccdir || exit 1;
utils/fix_data_dir.sh data/$data
echo extracted MFCCs
echo

## Alignment
steps/align_si.sh --nj 1 --cmd "$train_cmd" \
    data/$data data/lang_small_test exp/tri4 exp/align || exit 1
echo extracted Alignments
echo

# Alignment to TextGrids
for i in exp/align/ali.*.gz;
do $KALDI_ROOT/src/bin/ali-to-phones --ctm-output exp/tri4/final.mdl \
    ark:"gunzip -c $i|" -> ${i%.gz}.ctm;
done;

cd $root/asr/exp/align
#rm -r textgrids
mkdir textgrids

cat *.ctm > merged_alignment.txt
echo 
echo

cd ..
python3 tophones.py ##idtoPhones

sed 's/_B//g' align/merged_alignment2.txt > align/merged_alignment3.txt
sed 's/_S//g' align/merged_alignment3.txt > align/merged_alignment4.txt
sed 's/_I//g' align/merged_alignment4.txt > align/merged_alignment5.txt
sed 's/_E//g' align/merged_alignment5.txt > align/merged_alignment6.txt

## Create TextGrids ##
python3 splitAlignments.py
mv *.txt align/textgrids
cp $1 $root/asr/exp/align/textgrids

cd $root/asr/exp/
cp header.sh header align/textgrids

cd align/textgrids
mkdir etc
bash header.sh

cd ../..
praat --run topraat.praat
echo Created Textgrids
echo


## Extract Formants
praat --run vowel_space.praat align/textgrids results.txt 0.01 5 5500 0.025 50 75 600
cp -r $root/asr/exp/align/textgrids $root

echo Extracted textgrids
echo

## Extract Vowel Space
#rm -r $root/asr/etc
mkdir $root/asr/etc
cd align/textgrids
cp results.txt $root/asr/etc

cd $root/asr/etc
python3 ../local/vowel_space.py

mv $root/asr/etc/results.txt ..

cd ..
python3 local/vowel_space2.py

echo Extracted vowel_space
echo

rm -r mfcc etc results.txt exp/make_mfcc exp/align data/test/*


