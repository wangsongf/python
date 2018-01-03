import time

now = time.time()
print(now)

localtime = time.localtime(time.time())
print(localtime)

localtime = time.localtime(time.time())
formatTime = time.asctime(localtime)
print(formatTime)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())) 
  
# convert time to timestamp
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
