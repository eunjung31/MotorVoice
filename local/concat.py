import pandas as pd

df1 = pd.read_csv('csv/vq_pitch.csv')
df2 = pd.read_csv('csv/sr.csv')
df_12 = pd.merge(df1,df2, on='filename')
df_12.set_index('filename',inplace=True)

#df_12.to_csv('vq_F0_sr.csv')

df_3 = pd.read_csv('csv/phoneme.csv')
df_123 = pd.merge(df_12,df_3, on='filename')
df_123.set_index('filename',inplace=True)

#df_123.to_csv('vq_F0_sr_p.csv')

df_4 = pd.read_csv('csv/vowel_result.csv')
df_tot = pd.merge(df_123, df_4, on='filename')
df_tot.set_index('filename',inplace=True)

#df_tot.to_csv('total_json.csv')

df0 = pd.read_csv('csv/mfcc.csv')
df_tot2 = pd.merge(df_tot, df0, on='filename')
#df_tot2.set_index('filename',inplace=True)


fn = df_tot2[['filename']].values
fileName = fn.tolist()

#print(fileName[0][0])

df_tot2.to_csv('csv/'+'total.csv')
df_tot2.to_csv('result/'+fileName[0][0]+'.csv')
