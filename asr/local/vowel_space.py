
import sys,csv
results=[]

with open("results.txt") as f:
    data = f.readlines()[2]
    name = data.split("\t")[0]

with open("results.txt") as f:
    next(f) #skip header
    for line in f:
        columns=line.split("\t")
        name_prev = name
        name = columns[0]
        if (name_prev != name):
            with open((name_prev)+".txt",'w') as fwrite:
                writer = csv.writer(fwrite)
                fwrite.write("\n".join(results))
                fwrite.close()
                del results[:]
                results.append(line[0:-1])
        else:
            results.append(line[0:-1])

with open((name_prev)+".txt",'w') as fwrite:
    writer = csv.writer(fwrite)
    fwrite.write("\n".join(results))
    fwrite.close()


