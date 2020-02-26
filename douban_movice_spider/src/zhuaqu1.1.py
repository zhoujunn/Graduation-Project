#coding=utf-8
import urllib2
import time
import re
import os
import random
for k in range(1900,2019):
    for s in range(0,8000,20):
        url ="https://movie.douban.com/tag/"+str(k)+"?start="+str(s)+"&type=T"
        req = urllib2.Request(url)
        res= urllib2.urlopen(req)
        html = res.read()
        links = re.findall ("\<a href=\"(https:\/\/movie.douban.com\/subject\/.+?\/)",html)
        try:
            print links[0]
        except:
            break
        lin=open('/home/hadoop/links.txt','a+')
        for i in links:
            lin.write(i)
            lin.write('\n')
        lin.close()
        time.sleep(random.randint(2,8))

     
            

