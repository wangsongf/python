import os

if __name__ == "__main__":
    files = os.walk('/root/python/')     # 这里调用了方法，传入一个路径，返回一个可迭代对象
    for i in files:     # 开始迭代
        print('path_name: ', i[0])  # 输出当前路径
        print('dir_name : ', i[1])  # 当前目录下的目录
        print('file_name: ', i[2])  # 当前目录下的文件
        print('-----------------')