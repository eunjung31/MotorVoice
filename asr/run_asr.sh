#!/bin/bash
. ./path.sh

cd $root/asr

bash local/prepare.sh $1 # Preparation for ASR 

bash local/decode.sh # ASR Decoding

python3 local/calculate_phoneme.py # Calculate PCC, PCV, PCT

mv phoneme.csv $root/csv

echo
echo Extracted phoneme features
echo

bash local/align.sh $1 # Extract Vowel Space related Features

cp vowel_result.csv $root/csv

echo
echo Extracted vowel features
echo

