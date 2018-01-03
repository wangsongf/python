#抓百度网页对象，输出网页内容
from urllib import request 
req = request.urlopen("http://www.baidu.com")
print(req.read().decode("utf-8"))
#模拟真实浏览器
from urllib import request 
resq = request.Request("http://www.baidu.com");
resq.add_header("User-Agent","Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36")
req = request.urlopen(resq)
print(req.read().decode("utf-8"))
