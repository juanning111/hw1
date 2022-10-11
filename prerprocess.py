import csv
import re
import os

trainfile=open("csv2txt/train.csv", 'w', newline='', encoding='utf-8')
testfile=open("csv2txt/test.csv", 'w', newline='', encoding='utf-8')
validfile=open("csv2txt/valid.csv", 'w', newline='', encoding='utf-8')
trainwriter=csv.writer(trainfile)
testwriter=csv.writer(testfile)
validwriter=csv.writer(validfile)
trainlist=[]
testlist=[]
validlist=[]

path='Poetry-master/data'
files=os.listdir(path)

for file in files:
    f=open(path+'/'+file,'r',encoding='utf-8')
    reader=csv.reader(f)
    i=1
    for line in reader:
        l = [line[-1]]
        l.append(1)  # 添加分类标签
        if i%8==2:
            trainlist.append(l)
        elif i%160==3:
            testlist.append(l)
        elif i%160==7:
            validlist.append(l)
        i+=1

shibu=open("shibu_clean/shibu_clean.txt", 'r', encoding='utf-8')

for i in range(2000000):
    s=shibu.readline().strip()
    news = re.sub(r'[0-9]+', '', s)
    l = [news]
    l.append(0)
    if i%20==0:
        trainlist.append(l)
    elif i%400==1:
        testlist.append(l)
    elif i%400==2:
        validlist.append(l)

trainwriter.writerows(trainlist)
testwriter.writerows(testlist)
validwriter.writerows(validlist)