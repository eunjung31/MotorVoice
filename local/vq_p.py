#!/usr/bin/env python
# coding: utf-8

import sys
import pandas as pd

path = sys.argv[1]

filename = path.split('.')[0]


def vq_pitch(fileName):
    f = open(fileName, 'r', encoding='utf-8')
    name = fileName.split('/')[-1].split('.')[0] 
    vq_P_list = []
    for line in f.readlines():
        line = line.strip()
        if 'Jitter (local)' in line:
            jitter = line.split(': ')[1].split('%')[0]
            jitter = float(jitter)
            #print(jitter)
        elif 'Shimmer (local)' in line:
            shimmer = line.split(': ')[1].split('%')[0]
            shimmer = float(shimmer)
            #print(shimmer)
        elif 'Mean harmonics-to-noise ratio' in line:
            HNR = line.split(': ')[1].split(' dB')[0]
            HNR = float(HNR)
            #print(hnr)
        elif 'Number of voice breaks' in line:
            nVB = line.split(': ')[1]
            nVB = int(nVB)
            #print(nVB)
        elif 'Degree of voice breaks' in line:
            perVB = line.split(': ')[1].split('%')[0]
            perVB = float(perVB)

        elif 'Median pitch:' in line:
            medF0 = line.split(': ')[1].split(' Hz')[0]
            medF0 = float(medF0)

        elif 'Mean pitch:' in line:
            meanF0 = line.split(': ')[1].split(' Hz')[0]
            meanF0 = float(meanF0)

        elif 'Standard deviation:' in line:
            stdF0 = line.split(': ')[1].split(' Hz')[0]
            stdF0 = float(stdF0)

        elif 'Minimum pitch:' in line:
            minF0 = line.split(': ')[1].split(' Hz')[0]
            minF0 = float(minF0)

        elif 'Maximum pitch:' in line:
            maxF0 = line.split(': ')[1].split(' Hz')[0]
            maxF0 = float(maxF0)

            twenty_five = medF0 - (medF0 - minF0) /2 
            seventy_five = medF0 + (maxF0 - medF0) /2


    vq_P_dict = {'filename':name,'jitter':round(jitter,2), 'shimmer':round(shimmer,2),'HNR':round(HNR,2),'nVB':round(nVB,2), 'perVB':round(perVB,2), 'med':round(medF0,2), 'mean':round(meanF0,2),'std':round(stdF0,2), 'min':round(minF0,2), 'max':round(maxF0,2), 'twenty_five':round(twenty_five,2), 'seventy_five':round(seventy_five,2)}

    vq_P_list.append(vq_P_dict)
    
    vq_P_df = pd.DataFrame(vq_P_list)
    #    vq_P_df.set_index('filename', inplace=True)
    
    vq_P_df.to_csv('csv/vq_pitch.csv',index=False)

vq_pitch(filename)

