# MotorVoice
Feature extractor & Automatic Severity Classifier for Motor Speech Disorder
MotorVoice is a framework designed to extract speech features for automatic severity classification of motor speech disorder. The to-be-extracted features include voice quality-, prosody-, and pronunciation-related features. Please refer [1] for details. 

## Requirements
* praat 
* kaldi
* pandas
* scikit-learn
* librispeech 

## Features & Software
|Features|Software|
|---|---|
|voice quality features|Praat|
|prosody features - pitch|Praat|
|prosody features - speech rate|Praat(Parselmouth)|
|pronunciation features - Percentage of Correct Phonemes|kaldi*|
|pronunciation features - Degree of Vowel Distortion|kaldi(alignment),Praat|

Since MotorVoice exploits pretrained ASR model(tdnn model), it is highly dependent on phoneme inventories and language.
So far, experiments have been conducted on only Korean dysarthric speech. We aim to expand our research into other languages such as English, Chinese, Spanish, etc.
 
 
[1] Yeo, E. J., Kim, S., & Chung, M. (2021). Automatic Severity Classification of Korean Dysarthric Speech Using Phoneme-Level Pronunciation Features. Proc. Interspeech 2021, 4838-4842.

---
version https://git-lfs.github.com/spec/v1
oid sha256:b97596a5319d558c863615058fd689357bc25f74c95a2656082a78ee516e4f65
size 118
