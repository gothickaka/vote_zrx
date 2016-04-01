import requests
import time
from pytesser import *


a = 110001
while a <= 118000:
    b = str(a)[1:6]
    usrname = 'zrx'+b
    print usrname
    a = a + 1
    i = 0
    while i<=0:
        s = requests.session()
        picdata = s.get('http://www.21boya.cn/dianping/main/checkcode?type=reg&tick=1458055513')
        data = picdata.content
        f = open('1.gif','wb')
        f.write(data)
        f.close()
        checkcode = image_file_to_string('1.gif')
        checkcode = checkcode[0:5]
        print checkcode
        reppp = s.post('http://www.21boya.cn/dianping/ajax/main/ajax_reg.php', data=dict(action='reg2', uname=usrname, realname=usrname, pwd='abc123', mail=usrname+'@qq.com', code=checkcode, ipaduid=''))
        str1 = reppp.text
        if 'ok' in str1:
            i=i+1
        time.sleep(1)
