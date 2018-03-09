import time
import requests
from concurrent.futures import ThreadPoolExecutor

NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'

def fetch(a):
    r = requests.get(URL.format(a))
    return r.json()['args']['a']

start = time.time()
# 使用线程池（使用5个线程）
with ThreadPoolExecutor(max_workers=5) as executor:
  # 此处的map操作与原生的map函数功能一样
    for num, result in zip(NUMBERS, executor.map(fetch, NUMBERS)):
        print('fetch({}) = {}'.format(num, result))
print('cost time: {}'.format(time.time() - start))