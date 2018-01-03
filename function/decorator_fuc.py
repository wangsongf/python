import time

def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('spend %s'%(end - start))
    return inner

@show_time #foo=show_time(f)
def foo():
    print('foo...')
    time.sleep(1)
foo()

def bar():
    print('bar...')
    time.sleep(2)
bar()