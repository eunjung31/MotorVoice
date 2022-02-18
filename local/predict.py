import sklearn
import joblib
import pandas as pd
import numpy as np
from sklearn import preprocessing
import pickle
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

######### PREDICTION #################

selected2 = ['PCC','PCV','PCT','nVB','total_duration','vowel_space','VAI','FCR','F2','0','1','2','3','4','5','6','7','8','9','10','11','12']
category = ['category']
selected = selected2 + category

df_train = pd.read_csv('local/svmTrain.csv')
#df_train = sklearn.utils.shuffle(df_train)

df_test = pd.read_csv('csv/total.csv')

df_train = df_train[selected]
df_test = df_test[selected2]

y_train = df_train['category'].values
X_train = df_train.drop('category',axis=1).values

X_test = df_test.values

quantile_transformer = preprocessing.QuantileTransformer(random_state=0)

X_train = quantile_transformer.fit_transform(X_train)
X_test = quantile_transformer.transform(X_test)


clf = SVC(C=1, gamma=0.1, decision_function_shape='ovo')
clf.fit(X_train, y_train)

pred = clf.predict(X_test)

########### RHYTHM (FUTURE WORK) ##########
df_test = pd.read_csv('csv/resultPercent.csv')
df = df_test.drop(['0','1','2','3','4','5','6','7','8','9','10','11','12'], axis=1)


df['predicted'] = pred
############################################

################# CALCULATE CONDITION  #######################

#vq = ['jitter','shimmer','HNR','nVB','perVB']
#df = df_test[vq]
#df = df.copy()

#sample = {'jitter':1.90, 'shimmer':8.08, 'HNR':15.07, 'nVB':8.93, 'perVB':25.38}
#df = df.append(sample, ignore_index=True)

#sample2 = {'jitter':7.0, 'shimmer':27.0, 'HNR':6.0, 'nVB':25.0, 'perVB':100}
#df = df.append(sample2, ignore_index=True)

#sample3 = {'jitter':2.90, 'shimmer':30.0, 'HNR':20.0, 'nVB':13.0, 'perVB':50}
#df = df.append(sample3, ignore_index=True)

## calculate z-score
df['jit-z']= (df['jitter']-1.78)/0.63
df['shim-z']= (df['shimmer']-7.80)/2.48
df['hnr-z']= (df['HNR']-15.18)/2.80
df['nVb-z']= (df['nVB']-10.08)/4.28
df['perVb-z']= (df['perVB']-27.46)/15.54

#df['total'] = df['jitter'] + df['shimmer'] + df['HNR'] + df['nVB'] + df['perVB']


df.loc[df['jit-z'] < 0 , 'jit-z'] = 0
df.loc[df['shim-z'] < 0 , 'shim-z'] = 0
df.loc[df['hnr-z'] > 0 , 'hnr-z'] = 0
df.loc[df['nVb-z'] < 0 , 'nVb-z'] = 0
df.loc[df['perVb-z'] < 0 , 'perVb-z'] = 0


df['condition'] = 100 - ((abs(df['jit-z']) + abs(df['shim-z']) + abs(df['hnr-z']) + abs(df['nVb-z']) + abs(df['perVb-z'])))*5

df.condition = df.condition.astype(int)

#print(df)


############### Probability  ####################

prob = ['filename','nVB','speech_duration','PCC','PCV','PCT','vowel_space','FCR','VAI','F2']

#df = df_test[prob]
#df = df.copy()

sample = {'nVB':2, 'speech_duration':3, 'PCC':100, 'PCV':100, 'PCT':100, 'vowel_space':420000, 'FCR':0, 'VAI':2, 'F2':4}
#df = df.append(sample, ignore_index=True)

sample2 = {'nVB':25, 'speech_duration':50, 'PCC':0, 'PCV':0, 'PCT':0, 'vowel_space':0, 'FCR':4, 'VAI':0, 'F2':0}
#df = df.append(sample2, ignore_index=True)

#sample3 = {'jitter':2.90, 'shimmer':30.0, 'HNR':8.0, 'nVB':13.0, 'perVB':50}
#df = df.append(sample3, ignore_index=True)

## calculate z-score
df['nVb-z']= (df['nVB']-10.08)/4.27
df['Sr-z']= (df['speech_duration']-7.87)/4.84
df['PCC-z']= (df['PCC']-67.50)/33.35
df['PCV-z']= (df['PCV']-67.57)/33.67
df['PCT-z']= (df['PCT']-67.39)/33.46
df['VS-z']= (df['vowel_space']-90908)/80376
df['FCR-z']= (df['FCR']-1.43)/0.32
df['VAI-z']= (df['VAI']-0.73)/0.15
df['F2-z']= (df['F2']-1.63)/0.53

#df['total2'] = df['nVB'] + df['speech_duration'] + df['PCC'] + df['PCV'] + df['PCT'] \
#        + df['vowel_space'] + df['FCR'] + df['VAI'] + df['F2']

#df['total2'] = df['nVB'] + df['speech_duration'] + 100 + 100 + 100 \
#        + df['FCR'] + df['VAI'] + df['F2']

df.loc[df['nVb-z'] < 0 , 'nVb-z'] = 0
df.loc[df['Sr-z'] < 0 , 'Sr-z'] = 0
df.loc[df['PCC-z'] > 0 , 'PCC-z'] = 0
df.loc[df['PCV-z'] > 0 , 'PCV-z'] = 0
df.loc[df['PCT-z'] > 0 , 'PCT-z'] = 0
df.loc[df['VS-z'] > 0 , 'VS-z'] = 0
df.loc[df['FCR-z'] < 0 , 'FCR-z'] = 0
df.loc[df['VAI-z'] > 0 , 'VAI-z'] = 0
df.loc[df['F2-z'] > 0 , 'F2-z'] = 0

#df['probability'] = ((abs(df['nVb-z']) + abs(df['Sr-z']) + abs(df['PCC-z']) + abs(df['PCV-z']) + abs(df['PCT-z']) \
#       + abs(df['VS-z']) + abs(df['FCR-z']) + abs(df['VAI-z']) + abs(df['F2-z']))/df['total2'])

df['predicted2'] = df.predicted

df['condition2'] = df.condition

df['probability'] = ((abs(df['nVb-z']) + abs(df['Sr-z']) + abs(df['PCC-z']) + abs(df['PCV-z']) + abs(df['PCT-z']) \
       + abs(df['VS-z']) + abs(df['FCR-z']) + abs(df['VAI-z']) + abs(df['F2-z'])) * 7)

df.probability = df.probability.astype(int)


#print(df)




################ RESULT #####################
df.to_csv('csv/result.csv',index=False)
