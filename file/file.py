#coding: utf-8
#codes
f=open("test.txt","r")
f2=open("test2.txt","w")
# print(f.read())
for line in f:
    if "让我掉下眼泪的" in line:
        line=line.replace("让我掉下眼泪的","让我们彼此掉下眼泪的")
        f2.write(line)
    else:
        f2.write(line)
f.close()
f2.close()
