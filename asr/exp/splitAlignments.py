#!/bin/sh

import sys,csv
results=[]

#name = "F0037_CS_0001"
#name_fin = "M0155_CS_2004"

with open("align/merged_alignment6.txt") as f:
    data = f.readlines()[1]

    name = data.split("\t")[0]
   # print(name)
    
with open("align/merged_alignment6.txt") as f:
    for line in f:
        columns=line.split("\t")
        name_prev = name
        name = columns[0]
        if (name_prev != name):
            with open((name_prev)+".txt",'w') as fwrite:
                writer = csv.writer(fwrite)
                fwrite.write("\n".join(results))
                fwrite.close()
                #print name
                del results[:]
                results.append(line[0:-1])
        else:
            results.append(line[0:-1])
    
with open((name_prev)+".txt",'w') as fwrite:
    writer = csv.writer(fwrite)
    fwrite.write("\n".join(results))
    fwrite.close()
