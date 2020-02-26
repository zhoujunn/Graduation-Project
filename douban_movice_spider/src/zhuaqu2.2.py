#coding=utf-8
mids=set()
outs=open('/home/zhouxinjun/infonew.txt','w')
ins=open('/home/zhouxinjun/info1.txt','r')
for line in ins:
    mid,other= line.split('\t', 1)
    if mid not in mids:
        outs.write(line)
        mids.add(mid)
outs.close()
