
from urllib import request 
from urllib import parse

resq = request.Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult");
resq.add_header("User-Agent","Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36")
resq.add_header("Origin","http://www.thsrc.com.tw")
postDate = parse.urlencode([
        ("StartStation","2f940836-cedc-41ef-8e28-c2336ac8fe68"),
        ("EndStation","977abb69-413a-4ccf-a109-0272c24fd490"),
        ("SearchDate","2017/12/09"),
        ("SearchTime","21:30"),
        ("SearchWay","DepartureInMandarin")
        ]);
req = request.urlopen(resq,data=postDate.encode("utf-8"))
print(req.read().decode("utf-8"))
