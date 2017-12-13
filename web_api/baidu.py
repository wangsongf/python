import requests

data = requests.get('https://www.baidu.com/')
data.encoding='utf-8'

print(data.text)