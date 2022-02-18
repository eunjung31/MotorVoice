#!/bin/bash
. ./path.sh
. ./cmd.sh

cd $root/asr/data
cp prepare_data.py test

cd test
python3 prepare_data.py $1

cd $root/asr

for x in test ; do
    utils/utt2spk_to_spk2utt.pl data/$x/utt2spk > data/$x/spk2utt
    utils/validate_data_dir.sh data/$x
    utils/fix_data_dir.sh data/$x
done



