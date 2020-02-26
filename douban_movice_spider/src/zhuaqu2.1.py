#coding=utf-8
import urllib2
import time
import sys
import os
import re
import random
cishu=0
for line in sys.stdin:
    cishu=cishu+1
    headers={'Accept':'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8','Accept-language':'zh-CN,zh;q=0.9','Connection':'keep-alive','Cookie':'bid=ZgTRAjinX2E; __utma=30149280.1472938870.1523700243.1524143643.1524147843.34; __utmz=30149280.1524147843.34.27.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; ll="118227"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1524147741%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3D17863076876%26redir%3Dhttps%253A%252F%252Fmovie.douban.com%252F%26source%3DNone%26error%3D1011%22%5D; _pk_id.100001.4cf6=9a727c9b41624859.1523700240.37.1524147858.1524147741.; __yadk_uid=OcPKGZYtl99XzP5AYFXhYHLuCzwkCnSO; __utma=223695111.1516700935.1523700243.1524143665.1524147843.32; __utmz=223695111.1524147843.32.24.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; _vwo_uuid_v2=D16D5F2B4F9C8EE0130B4524E7BD1FDD1|71df4c78521fa7fb90f52c59c7c61a56; ps=y; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17648; ap=1; ue="643920085@qq.com"; dbcl2="176482122:RoxqF1eJwSk"; ck=LMc7; __utmc=30149280; __utmc=223695111; _pk_ses.100001.4cf6=*; __utmb=30149280.0.10.1524147843; __utmb=223695111.0.10.1524147843','Host':'movie.douban.com','Referer':'https://movie.douban.com/tag','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
    url=line
    req= urllib2.Request(url,headers=headers)
    res= urllib2.urlopen(req)
    html = res.read()
    did=re.findall("url=http:\/\/m.douban.com\/movie\/subject\/(.+?)\/",html)
    title=re.findall("\"v:itemreviewed\"\>(.+?)\<\/span\>",html)
    year=re.findall("class=\"year\"\>\((\d\d\d\d)\)",html)
    types=re.findall("\"v:genre\"\>(.+?)\<\/span\>",html)
    state=re.findall(">制片国家/地区:</span> (.+?)<br/>",html)
    score=re.findall("\"v:average\"\>(.+?)\<\/strong\>",html)
    snum=re.findall("\"v:votes\"\>(.+?)\<\/span\>",html)
    tnum=re.findall("status=P\"\>全部 (.+?) 条\<\/a\>",html)
    slen=len(score)
    tlen=len(types)
    ylen=len(year)
    dlen=len(state)
    if slen==0 or ylen==0  or  dlen==0:
        time.sleep(1)
        continue
    else:
        if tlen==0:
            if slen!=0:
                record=did[0]+'\t'+title[0]+'\t'+year[0]+'\t'+state[0]+'\t'+score[0]+'\t'+snum[0]+'\t'+tnum[0]
            else:
                record=did[0]+'\t'+title[0]+'\t'+year[0]+'\t'+state[0]
        elif tlen==1:
            record=did[0]+'\t'+title[0]+'\t'+year[0]+'\t'+types[0]+'\t'+state[0]+'\t'+score[0]+'\t'+snum[0]+'\t'+tnum[0]
        elif tlen==2:
            record=did[0]+'\t'+title[0]+'\t'+year[0]+'\t'+types[0]+'\\'+types[1]+'\t'+state[0]+'\t'+score[0]+'\t'+snum[0]+'\t'+tnum[0]
        elif tlen==3:
            record=did[0]+'\t'+title[0]+'\t'+year[0]+'\t'+types[0]+'\\'+types[1]+'\\'+types[2]+'\t'+state[0]+'\t'+score[0]+'\t'+snum[0]+'\t'+tnum[0]
        elif tlen==4:
            record=did[0]+'\t'+title[0]+'\t'+year[0]+'\t'+types[0]+'\\'+types[1]+'\\'+types[2]+'\\'+types[3]+'\t'+state[0]+'\t'+score[0]+'\t'+snum[0]+'\t'+tnum[0]
        elif tlen==5:
            record=did[0]+'\t'+title[0]+'\t'+year[0]+'\t'+types[0]+'\\'+types[1]+'\\'+types[2]+'\\'+types[3]+'\\'+types[4]+'\t'+state[0]+'\t'+score[0]+'\t'+snum[0]+'\t'+tnum[0]
        elif tlen==6:
            record=did[0]+'\t'+title[0]+'\t'+year[0]+'\t'+types[0]+'\\'+types[1]+'\\'+types[2]+'\\'+types[3]+'\\'+types[4]+'\\'+types[5]+'\t'+state[0]+'\t'+score[0]+'\t'+snum[0]+'\t'+tnum[0]
        else:
            record=did[0]+'\t'+title[0]+'\t'+year[0]+'\t'+state[0]+'\t'+score[0]+'\t'+snum[0]+'\t'+tnum[0]
    info=open('/home/zhouxinjun/info.txt','a+')
    info.write(record)
    print str(cishu)+'\t'+did[0]
    info.write('\n')
    info.close()
    time.sleep(random.randint(2,4))
