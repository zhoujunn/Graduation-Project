#coding=utf-8
lines=set()
outs=open('/home/hadoop/links2.txt','w')
ins=open('/home/hadoop/links.txt','r')
for line in ins:
    if line not in lines:
        outs.write(line)
        lines.add(line)
outs.close()

      
    

