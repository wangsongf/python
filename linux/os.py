# 仅列举所有的文件
from os import listdir
from os.path import isfile, join
mypath = '/root/python/' # src\app
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
# 使用 walk 递归搜索
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
print(f)