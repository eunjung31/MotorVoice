f = open('phones.txt', 'r')

list_p = []
list_n = []
for line in f.readlines():
    line = line.strip()
    phoneme = line.split(' ')[0]
    list_p.append(phoneme)

    number = line.split(' ')[1]
    list_n.append(number)

    dictionary = dict(zip(list_p, list_n))

print(dictionary)

