import joblib
import pandas as pd
import numpy as np


df = pd.read_csv('csv/total.csv')

#df = df_test.drop(['0','1','2','3','4','5','6','7','8','9','10','11','12'], axis=1)

#df['%V'] = 79.93
#df['deltaV'] =317.45
#df['deltaC'] = 49.26
#df['VarcoV'] = 79.01
#df['VarcoC'] = 43.19
#df['rPVIV'] = 288.97
#df['rPVIC'] = 54.25
#df['nPVIV'] = 74.28
#df['nPVIC'] = 46.20

#df['twenty_five'] = 135.41
#df['seventy_five'] = 311.75

############################################

## calculate z-score (vq)
df['jit-z']= (df['jitter']-1.78)/0.63
df['shim-z']= (df['shimmer']-7.80)/2.48
df['hnr-z']= (df['HNR']-15.18)/2.80
df['nVb-z']= (df['nVB']-10.08)/4.28
df['perVb-z']= (df['perVB']-27.46)/15.54


## calculate z-score (pitch)
df['med-z']= (df['med']-189.41)/52.21
df['avg-z']= (df['mean']-192.48)/51.31
df['std-z']= (df['std']-50.36)/24.61
df['min-z']= (df['min']-81.41)/31.29
df['max-z']= (df['max']-434.09)/150.79
df['25-z']= (df['twenty_five']-135.41)/34.39
df['75-z']= (df['seventy_five']-311.75)/85.91

## calculate z-score (vD)
df['vsa-z']= (df['vowel_space']-90908.9)/80376.2
df['fcr-z']= (df['FCR']-1.44)/0.32
df['vai-z']= (df['VAI']-0.73)/0.15
df['f2Ratio-z']= (df['F2']-1.63)/0.53

## calculate z-score (vD)
df['PCT-z']= (df['PCT']-67.57)/33.67
df['PCC-z']= (df['PCC']-67.39)/33.46
df['PCV-z']= (df['PCV']-67.50)/33.35


## calculate z-score (sR)
df['tD-z']= (df['total_duration']-7.87)/4.84
df['sD-z']= (df['speech_duration']-5.08)/4.44
df['sR-z']= (df['speaking_rate']-2.67)/0.86
df['aR-z']= (df['articulation_rate']-4.53)/1.41


## calculate z-score (Rhythm)
#df['pV-z']= (df['%V']-84.17)/6.55
#df['delta-z']= (df['deltaV']-754.73)/609.98
#df['varco-z']= (df['VarcoV']-85.09)/22.22
#df['pvis-z']= (df['VarcoV']-86.80)/19.50


#### PREPROCESS #############

df.loc[df['jit-z'] < 0 , 'jit-z'] = 0
df.loc[df['shim-z'] < 0 , 'shim-z'] = 0
df.loc[df['hnr-z'] > 0 , 'hnr-z'] = 0
df.loc[df['nVb-z'] < 0 , 'nVb-z'] = 0
df.loc[df['perVb-z'] < 0 , 'perVb-z'] = 0


df.loc[df['med-z'] > 0 , 'med-z'] = 0
df.loc[df['avg-z'] > 0 , 'avg-z'] = 0
df.loc[df['std-z'] > 0 , 'std-z'] = 0
df.loc[df['min-z'] > 0 , 'min-z'] = 0
df.loc[df['max-z'] > 0 , 'max-z'] = 0
df.loc[df['25-z'] > 0 , '25-z'] = 0
df.loc[df['75-z'] > 0 , '75-z'] = 0


df.loc[df['vsa-z'] > 0 , 'vsa-z'] = 0
df.loc[df['fcr-z'] < 0 , 'fcr-z'] = 0
df.loc[df['vai-z'] > 0 , 'vai-z'] = 0
df.loc[df['f2Ratio-z'] > 0 , 'f2Ratio-z'] = 0


df.loc[df['PCT-z'] > 0 , 'PCT-z'] = 0
df.loc[df['PCC-z'] > 0 , 'PCC-z'] = 0
df.loc[df['PCV-z'] > 0 , 'PCV-z'] = 0


df.loc[df['tD-z'] < 0 , 'tD-z'] = 0
df.loc[df['sD-z'] < 0 , 'sD-z'] = 0
df.loc[df['sR-z'] > 0 , 'sR-z'] = 0
df.loc[df['aR-z'] > 0 , 'aR-z'] = 0


#df.loc[df['pV-z'] < 0 , 'pV-z'] = 0
#df.loc[df['delta-z'] < 0 , 'delta-z'] = 0
#df.loc[df['varco-z'] > 0 , 'varco-z'] = 0
#df.loc[df['pvis-z'] > 0 , 'pvis-z'] = 0

###### p -value
import scipy.stats

df['jitt_p'] = scipy.stats.norm.sf(abs(df['jit-z'])) * 2 *100
df['shim_p'] = scipy.stats.norm.sf(abs(df['shim-z'])) * 2 *100
df['hnr_p'] = scipy.stats.norm.sf(abs(df['hnr-z'])) * 2 *100
df['nVb_p'] = scipy.stats.norm.sf(abs(df['nVb-z'])) * 2 *100
df['perVb_p'] = scipy.stats.norm.sf(abs(df['perVb-z'])) * 2 *100

df.jitt_p = df.jitt_p.astype(int)
df.shim_p = df.shim_p.astype(int)
df.hnr_p = df.hnr_p.astype(int)
df.nVb_p = df.nVb_p.astype(int)
df.perVb_p = df.perVb_p.astype(int)


df['med_p'] = scipy.stats.norm.sf(abs(df['med-z'])) * 2 *100
df['avg_p'] = scipy.stats.norm.sf(abs(df['avg-z'])) * 2 *100
df['std_p'] = scipy.stats.norm.sf(abs(df['std-z'])) * 2 *100
df['min_p'] = scipy.stats.norm.sf(abs(df['min-z'])) * 2 *100
df['max_p'] = scipy.stats.norm.sf(abs(df['max-z'])) * 2 *100
df['tf_p'] = scipy.stats.norm.sf(abs(df['25-z'])) * 2 *100
df['sf_p'] = scipy.stats.norm.sf(abs(df['75-z'])) * 2 *100

df.med_p = df.med_p.astype(int)
df.avg_p = df.avg_p.astype(int)
df.std_p = df.std_p.astype(int)
df.min_p = df.min_p.astype(int)
df.max_p = df.max_p.astype(int)
df.tf_p = df.tf_p.astype(int)
df.sf_p = df.sf_p.astype(int)


df['vsa_p'] = scipy.stats.norm.sf(abs(df['vsa-z'])) * 2 *100
df['fcr_p'] = scipy.stats.norm.sf(abs(df['fcr-z'])) * 2 *100
df['vai_p'] = scipy.stats.norm.sf(abs(df['vai-z'])) * 2 *100
df['f2Ratio_p'] = scipy.stats.norm.sf(abs(df['f2Ratio-z'])) * 2 *100

df.vsa_p = df.vsa_p.astype(int)
df.fcr_p = df.fcr_p.astype(int)
df.vai_p = df.vai_p.astype(int)
df.f2Ratio_p = df.f2Ratio_p.astype(int)


df['PCT_p'] = scipy.stats.norm.sf(abs(df['PCT-z'])) * 2 *100
df['PCC_p'] = scipy.stats.norm.sf(abs(df['PCC-z'])) * 2 *100
df['PCV_p'] = scipy.stats.norm.sf(abs(df['PCV-z'])) * 2 *100

df.PCT_p = df.PCT_p.astype(int)
df.PCC_p = df.PCC_p.astype(int)
df.PCV_p = df.PCV_p.astype(int)


df['tD_p'] = scipy.stats.norm.sf(abs(df['tD-z'])) * 2 *100
df['sD_p'] = scipy.stats.norm.sf(abs(df['sD-z'])) * 2 *100
df['sR_p'] = scipy.stats.norm.sf(abs(df['sR-z'])) * 2 *100
df['aR_p'] = scipy.stats.norm.sf(abs(df['aR-z'])) * 2 *100

df.tD_p = df.tD_p.astype(int)
df.sD_p = df.sD_p.astype(int)
df.sR_p = df.sR_p.astype(int)
df.aR_p = df.aR_p.astype(int)


#df['pV_p'] = scipy.stats.norm.sf(abs(df['pV-z'])) * 2 *100
#df['delta_p'] = scipy.stats.norm.sf(abs(df['delta-z'])) * 2 *100
#df['varco_p'] = scipy.stats.norm.sf(abs(df['varco-z'])) * 2 *100
#df['pvis_p'] = scipy.stats.norm.sf(abs(df['pvis-z'])) * 2 *100

#df.pV_p = df.pV_p.astype(int)
#df.delta_p = df.delta_p.astype(int)
#df.varco_p = df.varco_p.astype(int)
#df.pvis_p = df.pvis_p.astype(int)

#print(df)

################ RESULT #####################
df.to_csv('csv/resultPercent.csv',index=False)
