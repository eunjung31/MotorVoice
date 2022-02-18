# -*- coding: utf-8 -*-
from jamo import h2j, j2hcj
import sys

sys.stdout = open('phoneme.csv', 'w', encoding='utf-8')

f = open('decoded_result/per_utt', 'r', encoding='utf-8')

consonant = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ',
        'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ',
        'ㄳ','ㄵ','ㄶ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅄ']

vowel = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ',
       'ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']

ref=[]
hyp=[]
op=[]


print("%s,%s,%s,%s" % ("filename", "PCT", "PCC", "PCV"))


for line in f.readlines():
    line = line.strip()
    word_list = [word for word in line.split(' ')]
    word_list = ' '.join(word_list).split()

    if word_list[1] == 'ref':
        ref.append(word_list)
    if word_list[1] == 'hyp':
        hyp.append(word_list)
    if word_list[1] == 'op' :
        op.append(word_list)

for i in range(len(ref)):
    correct = []
    tc, tv = 0, 0
    c,v = 0, 0

    length = len(ref[i])

    for j in range(2, len(ref[i])):
        ref[i][j] = list(j2hcj(h2j(ref[i][j])))
        hyp[i][j] = list(j2hcj(h2j(hyp[i][j])))

        a,b = ref[i][j], hyp[i][j]

       # print(a, b)

        for char in a :
            if char in consonant :
                tc += 1
            elif char in vowel : 
                tv += 1

        for char in a:
            if char in b :
                correct.append(char)

    for character in correct :
        if character in consonant :
            c += 1
        elif character in vowel :
            v += 1

    print("%s,%.2f,%.2f,%.2f" % (ref[i][0], ((c+v)/(tc+tv))*100, c/tc*100, v/tv*100))


