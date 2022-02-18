import os
import librosa
import numpy as np
import sys


sys.stdout = open('csv/mfcc.csv','w')

path = sys.argv[1]

print("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % ("filename", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))

fn = path.split('/')[-1].split('.')[0]
y, sr = librosa.load(path)
S = librosa.feature.melspectrogram(y, sr=sr)
log_S = librosa.power_to_db(S, ref=np.max)
mfcc_1 = librosa.feature.mfcc(S=log_S, n_mfcc=13)
mfcc1 = np.average(mfcc_1, axis=1)
            
print("%s,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f" % (fn, mfcc1[0], mfcc1[1], mfcc1[2], mfcc1[3], mfcc1[4], mfcc1[5], mfcc1[6], mfcc1[7], mfcc1[8], mfcc1[9], mfcc1[10], mfcc1[11], mfcc1[12]))
