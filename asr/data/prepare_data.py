#This file is to create spk2gender, wav.scp, text, and utt2spk
import os
import codecs
import sys

path=sys.argv[1]
fn = path.split('/')[-1]

#speak2gender
def spk2gender():
   # f = open("spk2gender", 'w')
    f= open('spk2gender','w')
    f.write("speaker m\n")
    f.close()

#wav.scp
def wav(path):
    f = open('wav.scp','w')
    utt = fn.rsplit('.', 1)[0]
    full_dir = path
    f.write("%s %s\n" %(utt, full_dir))
    f.close()

#text
def text(path):
    f = codecs.open("text", 'w', encoding = 'utf-8')
    
    txtDir = path.split('.')[0]+'.txt'
    g = codecs.open(txtDir, 'r', encoding = 'utf-8')
    
    lines = g.readline()
    lines = lines.strip()
                
    utt = fn.rsplit('.', 1)[0]
                
    f.write("%s %s\n" %(utt, lines))
    
    g.close()
    f.close()

#utt2spk
def utt2spk(path):
    f = open('utt2spk','w')
    utt = fn.rsplit('.', 1)[0]
    f.write('%s speaker\n' %(utt))

    f.close()

spk2gender()
wav(path)
text(path)
utt2spk(path)
