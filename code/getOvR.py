__author__ = 'ocean'
import csv
import codecs
import sys
import random
reload(sys)
sys.setdefaultencoding('utf8')
filename="80-full-OvR-1vsRest.csv"
open(filename, 'w').close()
d={'AIM':1,'CTR':2,'OWN':3,'BKG':4,'OTH':5,'BAS':6,'TXT':7}
senlist=[]
with open('80-full-random-numberlabel.csv', 'rb') as csvfile: #80-full-random-numberlabel
    reader = csv.reader(csvfile, delimiter=',')
    cols=[0,1,2]
    for row in reader:
        content = list(row[i] for i in cols)
        strID = str(content[0]).strip()
        strlabel=str(content[1]).strip()
        sentence = str(content[2]).strip()
        sepsent=sentence.split()
        strremove=str(sepsent[0])+' '
        sentence=sentence.replace(strremove,'')
        if strlabel.strip() == 'AIM':
            strRow=strID+','+1+','+sentence+'\n'
        else:
            strRow=strID+','+'0'+','+sentence+'\n'

        senlist.append(strRow)


with codecs.open(filename, 'a', encoding='utf-8') as f:
    n=len(senlist)
    ranlist = random.sample(range(0,n-1),  n-1)
    for idx in ranlist:
        s=senlist[idx]
        f.write(s)
