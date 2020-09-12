#create dictionary first using wordlist
import pandas as pd
import numpy as np
from nltk.tokenize import RegexpTokenizer
file = open ('wordlist.txt', mode = 'r', encoding='utf8')
Dict = {}
i = 1
for word in file:
word_strip = word.rstrip()
if word_strip in Dict:
i = i
else:
Dict[word_strip] = i
i = i + 1

#create word count array
cnt = 0
stri = pd.read_csv('train_input_mlp.csv',header = None, encoding='ISO-8859-1')
word_cnt = [[] for l in range(0,len(stri))]
for line in stri[0]:
tokenizer1 = RegexpTokenizer(r'[A-Z]\w+|[a-z]\w+')
reg_token = tokenizer1.tokenize(line)
reg = [word.lower() for word in reg_token]
sum = []
i = 0
j = 0
k = 0
word_vctr = [[] for i in range(0,len(reg))]
for each in reg:
for i in range(0,len(Dict)):
word_vctr[j].append(0)
if each in Dict:
k = Dict[each]
word_vctr[j][k] = 1
j = j + 1
word_cnt[cnt] = word_vctr[0]
for i in range(1,len(reg)):
word_cnt[cnt] = [a + b for a, b in zip(word_cnt[cnt], word_vctr[i])]
cnt = cnt + 1