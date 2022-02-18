#!/bin/bash
. ./path.sh

#export root="/home/eunjung/automatic_classifier"
#set -ex

stage=0
path2=`pwd`
path=$1

cd $root

#### Delete Previous files ###

if [ $stage -le 1 ]; then 
rm -r csv result asr/data/test
mkdir csv result asr/data/test
fi

### Preprocess Text (Mecab) ###
if [ $stage -le 2 ]; then 
python3 local/mecab.py $1 || exit 1;
echo Preprocessed Texts
echo
fi


### Preprocess Audio (16k to 8k) ###
if [ $stage -le 3 ]; then 
split=($(echo $1| tr "." "\n"))
base=${split[0]}
wav=${base}".wav"
new=${base}_"8k.wav"

sox "$wav" -r 8k -b 16 "$new"

mv $new $1
echo Preprocessed Audios 
echo 
fi

### Extract MFCCs ###
if [ $stage -le 4 ]; then 
python3 local/extract_mfcc.py $1 || exit 1;

echo Extracted MFCCs
echo
fi


### Extract VoiceQuality, Prosody features ###
if [ $stage -le 5 ]; then 
python3 local/voice_report.py $1 || exit 1;

python3 local/vq_p.py $1 || exit 1;
python3 local/sr.py $1 || exit 1;

echo Extracted Voice Report Features
echo
fi

### Extract ASR
if [ $stage -le 6 ]; then 
cd asr

bash run_asr.sh $1 || exit 1;

fi
echo Extracted Phoneme-Related Features 


echo
echo ============================================
echo *************PREDICTING SEVERITY************
echo ============================================
echo

if [ $stage -le 7 ]; then 

cd $root
python3 local/concat.py || exit 1;

python3 local/toPercent.py || exit 1;
python3 local/predict.py || exit 1;
python3 local/toJson.py || exit 1;

echo
echo DONE
fi
