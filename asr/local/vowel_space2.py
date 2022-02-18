import os
import sys

sys.stdout = open('vowel_result.csv','w')

print("%s,%s,%s,%s,%s" %("filename", "vowel_space", "VAI", "FCR", "F2"))

root = r"etc/"

for r, d, files in os.walk(root):
    for filename in files:

        if filename.endswith(".txt"):
            path = os.path.join(r, filename)
            f = open(path, 'r')
            
            list_O_f1 = []
            list_E_f1 = []
            list_A_f1 = []
            list_I_f1 = []
    
            list_O_f2 = []
            list_E_f2 = []
            list_A_f2 = []
            list_I_f2 = []
            
            for line in f.readlines():
                line=line.strip()
                vowel = line.split('\t')[2]
                f1 = line.split('\t')[6]
                f2 = line.split('\t')[7]  
            
                if 'oo' or 'uu' in vowel:
                    list_O_f1.append(int(f1))
                    list_O_f2.append(int(f2))
                
                if 'ee' in vowel:
                    list_E_f1.append(int(f1))
                    list_E_f2.append(int(f2))
                
                if 'aa' in vowel:
                    list_A_f1.append(int(f1))
                    list_A_f2.append(int(f2))
                
                if 'ii' in vowel:
                    list_I_f1.append(int(f1))
                    list_I_f2.append(int(f2))
       
            f1_O = sum(list_O_f1)/len(list_O_f1)
            f2_O = sum(list_O_f2)/len(list_O_f2)

            f1_E = sum(list_E_f1)/len(list_E_f1)
            f2_E = sum(list_E_f2)/len(list_E_f2)
            
            
            f1_A = sum(list_A_f1)/len(list_A_f1)
            f2_A = sum(list_A_f2)/len(list_A_f2)    
            
            f1_I = sum(list_I_f1)/len(list_I_f1)
            f2_I = sum(list_I_f2)/len(list_I_f2)

            vowel_space = float(1/2*abs((f2_I*f1_E+f2_E*f1_A+f2_A*f1_O+f2_O*f1_I)-(f1_I*f2_E+f1_E*f2_A+f1_A*f2_O+f1_O*f2_I)))
            VAI = float((f2_I+f1_A)/(f1_I+f1_O+f2_O+f2_A))
            FCR = float((f2_O+f2_A+f1_I+f1_O)/(f2_I+f1_A))
            F2 = float(f2_I/f2_O)
           
            print("%s,%.2f,%.2f,%.2f,%.2f" %(filename[:-4], vowel_space, VAI, FCR, F2))
