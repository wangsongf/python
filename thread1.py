import time
import requests

NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'

# 获取网络请求结果
def fetch(a):
    r = requests.get(URL.format(a))
    return r.json()['args']['a']

# 开始时间
start = time.time()

for num in NUMBERS:
    result = fetch(num)
    print('fetch({}) = {}'.format(num, result))
# 计算花费的时间
print('cost time: {}'.format(time.time() - start))