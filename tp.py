# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:00:08 2018

@author: admin
"""
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.corpus import words
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
propernoun=[]
commonnoun=[]
ws=[]
sent=''
phrase=""
with open('Sales, Retail, Business Development_Area_ Territory Manager_phrase.txt', 'r') as myfile:
  sentence = myfile.read()
  sentence=sentence.lower()
for i in sentence:
    j+=1    
    if (ord(i)>=ord('a') and  ord(i)<=ord('z')) or (ord(i)==ord('"')) or (ord(i)==ord('@') or ((ord(i)==ord('.') and sentence[j+1]=='c'))):
        s+=i
        p+=1
        
    else:
        if p>0 and s[p-1]!=' ':
            s+=" "
            p+=1
            
for i in range (0,len(s)):
    if  i<(len(s)-1) and s[i]!='"':
        phrase+=s[i]
    else:
        l.append(phrase)
        #l[c]=phrase
        #c+=1
        phrase=""
for j in range(1,len(l),2):
    fl.append(l[j])
print("The total number of phrases are",len(fl)) 
for i in fl:
    ws.append()=word_tokenize(sentence)
    ts=pos_tag(ws)
nouns = [word for word,pos in ts if pos == 'NN'or pos=='NNP' or pos=='NNS']
word_list = words.words()
for i in nouns:
    if lemmatizer.lemmatize(i) not in word_list :
        propernoun.append(i.capitalize())    
    else:
        commonnoun.append(i)
        
print(propernoun)
print(commonnoun)
