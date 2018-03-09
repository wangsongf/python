import functools
 
def log(func):
    @functools.wraps(func)     #为了校正函数签名，最好写上
    def wrapper(*args,**kw):
        print('begin call')
        f = func(*args,**kw)
        print('end call')
        return f
    return wrapper
 
@log
def hah():
    print('hahahaha')
 
hah()