#coding=utf-8
from pytesser import *
import requests
import time

a = 110001
while a <= 118000:
    b = str(a)[1:6]
    usrname = 'zrx'+b
    print usrname
    a = a + 1
    s = requests.session()
    s.post('http://www.21boya.cn/dianping/ajax/main/ajax_reg.php',data=dict(action='login',uname=usrname,pwd='abc123'))
    i = 0
    while i<=4:
        picdata = s.get('http://www.21boya.cn/dianping/main/checkcode?type=fairytale2015&tick=1458019958000')
        data = picdata.content
        f = open('1.gif','wb')
        f.write(data)
        f.close()
        checkcode = image_file_to_string('1.gif')
        checkcode = checkcode[0:5]
        print checkcode
        reppp = s.post('http://www.21boya.cn/dianping/ajax/main/Microfairytale2016/vote.php',data=dict(pid =16,wid=3676,code=checkcode))
        str1 = reppp.text
        print str1
        if '\u6295\u7968\u6210\u529f' in str1:
            i=i+1
        elif '\u60a8\u4eca\u5929\u6295\u7968\u6b21\u6570\u5df2\u7ecf\u8d85\u8fc7\u6700\u5927\u503c' in str1:
            break
        time.sleep(1)