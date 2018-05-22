# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:19:11 2018

@author: admin
"""
from nltk import word_tokenize,sent_tokenize, pos_tag, ne_chunk
from nltk.corpus import words,stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import random
import json
import datetime
import dateutil.parser as parser
now = datetime.datetime.now()
from nltk.corpus import wordnet as wn
skills=[]
Prob={}
Sent=[]
sen=[]
ts=[]
aw=[]
cb=[]
Refined=[]
file_sentence={}
filename = input('Enter a filename: ')
with open(filename, 'r',encoding='utf-8-sig') as myfile:
  txt = myfile.read()
dd=json.loads(txt)
for i in range(0,len(dd["data"]["CandidateData"][0]["SkillSetDetails"])):
    skills.append(dd["data"]["CandidateData"][0]["SkillSetDetails"][i]['skillname'])
for i in range(0,len(dd["data"]["CandidateData"][0]["EmployementsHistoryDetails"]["EmployementHistoryData"])):
    cb.append(dd["data"]["CandidateData"][0]["EmployementsHistoryDetails"]["EmployementHistoryData"][i]["CompanyBlock"])
Reference={}
RP={}
RW={}
Management=['administered','analyzed','appointed','approved','assigned','attained','authorized','chaired','considered','consolidated','contracted','controlled','converted','coordinated','decided','delegated','developed','directed','eliminated','emphasized','enforced','enhanced','established','executed','generated','handled','headed','hired','hosted','improved','incorporated','increased','initiated','inspected','instituted','led','managed','merged','motivated','organized','originated','overhauled','oversaw','planned','presided','prioritized','produced','recommended','reorganized','released','replaced','restored','reviewed','scheduled streamlined','strengthened','supervised','terminated','addressed','advertised','arbitrated','arranged','articulated','authored','clarified','collaborated','communicated','composed','condensed','conferred','consulted','contacted','conveyed','convinced','corresponded','debated','defined','described','developed','directed','discussed','drafted','edited','elicited','enlisted','explained','expressed','formulated','furnished','incorporated','influenced','interacted','interpreted','interviewed','involved','joined','judged','lectured','listened','marketed','mediated','moderated','negotiated','observed','outlined','participated','persuaded','presented','promoted','proposed','publicized','reconciled','recruited','referred','reinforced','reported','resolved','responded','solicited','specified','spoke','suggested','summarized','synthesized','translated','wrote']
Organization=['approved','arranged','cataloged','categorized','charted','classified','collected','compiled','corresponded','distributed','executed','filed','generated','implemented','incorporated','inspected','logged','maintained','monitored','obtained','operated','ordered','organized','prepared','provided','purchased','recorded','registered','reserved','responded','reviewed','routed','scheduled','screened','set up','submitted','supplied','standardized','systematized','updated','validated','verified']
Research=['analyzed','clarified','collected compared','conducted','critiqued','detected','determined','diagnosed','evaluated','examined','experimented','explored','extracted','formulated','gathered','identified','inspected','interpreted','interviewed','invented','investigated','located','measured','organized','researched','searched','solved','summarized','surveyed','systematized','tested']
Technical=['adapted','assembled','built','calculated','coded','computed','conserved','constructed','converted','debugged','designed','determined','developed','engineered','fabricated','fortified','installed','maintained','operated','overhauled','printed','processed','programmed','rectified','regulated','remodeled','repaired','replaced','restored','solved','specialized','standardized','studied','upgraded','utilized']
for i in Management:
    Reference[lemmatizer.lemmatize(i,'v')]='management'
for i in Research:
    Reference[lemmatizer.lemmatize(i,'v')]='research'
for i in Technical:
    Reference[lemmatizer.lemmatize(i,'v')]='technical'
for i in Organization:
    Reference[lemmatizer.lemmatize(i,'v')]='organization'

sent=[]
for i in cb:
    ws=word_tokenize(i)
    sent=sent_tokenize(i)
    Sent.append(sent)
'''
for i in sen:
    if len(i)>2 and i not in Sent:
        Sent.append(i)
'''
stop_words = list(stopwords.words('english'))

for i in Sent:
    for k in i:
        refined_phrase=''
        ws=list(word_tokenize(k))
        for j in ws:
            if j not in stop_words:
                #q=lemmatizer.lemmatize(j.lower(),'v')
                q=j.lower()                
                refined_phrase+=q+' '
        Refined.append(refined_phrase)
ws=[]
m=o=t=r=comm=0
for i in Refined:
    ws.append(list(word_tokenize(i)))
for i in range(0,len(Refined)):
    for j in range(0,len(ws[i])):
        if lemmatizer.lemmatize(ws[i][j],'v') in Reference.keys():
            RP[Refined[i]]=Reference[lemmatizer.lemmatize(ws[i][j],'v')]
            RW[ws[i][j]]=Reference[lemmatizer.lemmatize(ws[i][j],'v')]

for i in RP.values():
    if(i.lower()=='technical'):
        t+=1
    elif(i.lower()=='management'):
        m+=1
    elif(i.lower()=='research'):
        r+=1
    else:
        o+=1            
typ=[m,o,r,t]
categ=['management','organization','research','technical']
max=0
sum=m+o+r+t
for i in range(0,len(typ)):
    if(typ[i]>max):
        maxc=categ[i]
        max=typ[i]
print('This profile is a ',maxc,'profile')
        
for i in range(0,len(categ)):
    Prob[categ[i]]=typ[i]/sum
print("The Probabilities are-:\n")
print(Prob)