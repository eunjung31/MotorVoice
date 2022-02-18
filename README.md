# MotorVoice
Feature extractor & Automatic Severity Classifier for Motor Speech Disorder
MotorVoice is a framework designed to extract speech features for automatic severity classification of motor speech disorder. The to-be-extracted features include voice quality-, prosody-, and pronunciation-related features. Please refer [1] for details. 

So far, Experiments have been conducted on only Korean dysarthric speech. We are aiming to extend our research to other languages such as English, Chinese, Spanish, etc.

## Requirements
* praat 
* kaldi
* pandas
* scikit-learn
* librispeech 

## Features & Software
|---|---|
|voice quality features|Praat|
|prosody features - pitch|Praat|
|prosody features - speech rate|Praat(Parselmouth)|
|pronunciation features - Percentage of Correct Phonemes|kaldi*|
|pronunciation features - Degree of Vowel Distortion|kaldi(alignment),Praat|

---
version https://git-lfs.github.com/spec/v1
oid sha256:b97596a5319d558c863615058fd689357bc25f74c95a2656082a78ee516e4f65
size 118
