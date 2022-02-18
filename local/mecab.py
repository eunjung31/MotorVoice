from konlpy.tag import Mecab
import os
import codecs
import sys

path = sys.argv[1]
new_path = path.split('.')[0] + '.txt'

mecab = Mecab()
#
with codecs.open(new_path,'r') as f:
    line = f.readline()
    line_list = mecab.morphs(line)
    new_string = ' '.join(line_list)

with open(new_path,'w',encoding='utf-8') as f:
    f.write(new_string)
