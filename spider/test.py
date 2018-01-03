import time
import requests
from bs4 import BeautifulSoup

def kill_captcha(data):
    with open('captcha.png', 'wb') as fp:
        fp.write(data)
    return raw_input('captcha : ')

def login(username, password, oncaptcha):
    session = requests.session()

    _xsrf = BeautifulSoup(session.get('https://www.zhihu.com/#signin').content).find('input', attrs={'name': '_xsrf'})['value']
    captcha_content = session.get('http://www.zhihu.com/captcha.gif?r=%d' % (time.time() * 1000)).content
    data = {
        '_xsrf': _xsrf,
        'email': username,
        'password': password,
        'remember_me': 'true',
        'captcha': oncaptcha(captcha_content)
    }
    resp = session.post('http://www.zhihu.com/login/email', data).content
    assert '\u767b\u9646\u6210\u529f' in resp
    return session

if __name__ == '__main__':
    session = login('wsf5862458@163.com', 'wsf123', kill_captcha)
    print(BeautifulSoup(session.get("https://www.zhihu.com").content).find('span', class_='name').getText())