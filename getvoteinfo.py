# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib
from email.mime.text import *
import smtplib
import time

while True:
    i = 0
    xc = u'星辰'
    f = open('1.txt','wb')
    while i <= 0:
        data = requests.get('http://www.21boya.cn/dianping/tale2016/works?type=1&page='+str(i)+'&st_other4=0&title=')
        data.encoding = 'utf8'
        soup = BeautifulSoup(data.text, 'lxml')
        titles = soup.select('div.it_winfo > div > div.wic_winfo > span')
        names = soup.select('div.it_winfo > div > div.wic_winfo > p')
        numbers = soup.select('div.it_winfo > div > div.wic_handler.clearfix > span > span.num_txt > span')
        imgs = soup.select('div.it_winfo > a > span')
        for title, name, number, img in zip(titles, names, numbers, imgs):
            # if xc in name.get('title'):
            #     a = u'第' + str(i+1) + u'页    ' + title.get('title') + '    ' + name.get('title') + '    ' + number.get_text()
            #     f.write(a.encode('utf8'))
            sms = title.get('title') + '    ' + name.get('title') + '    ' + number.get_text()+'\r'
            f.write(sms.encode('utf8'))
            print sms
            #保存图片到本地
            # src = 'http://www.21boya.cn'+img.get('data-url')
            # urllib.urlretrieve(src, '%s.jpg' % title.get('title'))
        i = i + 1
    f.close()

    # f = open('1.txt','r')
    # msg = MIMEText(f.read())
    # msg['Subject'] = 'vote'
    # msg['From'] = 'yangyishun@kedacom.com'
    # msg['To'] = 'uk.yy@163.com'
    # s = smtplib.SMTP('szmail.kedacom.com',25)
    # s.login('yangyishun', '******')
    # s.sendmail( 'yangyishun@kedacom.com', 'uk.yy@163.com', msg.as_string())
    # s.quit()
    # print 'OK!!!'
    print '==========================================================='
    time.sleep(60)