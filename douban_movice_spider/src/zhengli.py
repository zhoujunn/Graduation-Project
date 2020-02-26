#coding=utf-8
import sys
for line in sys.stdin:
    line=line.strip()
    t=len(line.split('\t',7))
    if t==8:
        record=line
    else:
        did,title,year,state,score,snum,tnum=line.split('\t',6)
        record=did+'\t'+title+'\t'+year+'\t'+'NULL'+'\t'+state+'\t'+score+'\t'+snum+'\t'+tnum
    records=open('/home/hadoop/records.txt','a+')
    records.write(record)
    records.write('\n')
    records.close()
        
    

