import os
writepath = '/root/python/file/'
# 可以根据文件是否存在选择写入模式
mode = 'a' if os.path.exists(writepath) else 'w'

# 使用 with 方法能够自动处理异常
with open("file.dat",mode) as f:
    f.write('write success')
    #...
    # 操作完毕之后记得关闭文件
    #f.close()

# 读取文件内容
message = f.read()
print(message)