import sys

f = open('align/phones.txt', 'r')

list_p = []
list_n = []
for line in f.readlines():
    line = line.strip()
    phoneme = line.split(' ')[0]
    list_p.append(phoneme)

    number = line.split(' ')[1]
    list_n.append(number)
    n_p = dict(zip(list_n, list_p))

#print(dictionary)

g = open('align/merged_alignment.txt', 'r')

sys.stdout = open('align/merged_alignment2.txt','w')

for line in g.readlines():
    line = line.strip()
    num = line.split(' ')[-1]
    base1 = line.split(' ')[0]
    base2 = line.split(' ')[1]
    base3 = line.split(' ')[2]
    base4 = line.split(' ')[3]
    phone = n_p[num]
   
    print("%s\t%s\t%s\t%s\t%s" % (base1, base2, base3, base4, phone))
