#coding=utf-8

def aJob(arg):
    """
    提供给多线程调用
    """
    import threading
    t = threading.current_thread()
    print(str(arg)+"current thread name is:"+t.getName()+"\n")


def multiThread():
    """
    多线程任务执行
    """
    from multiprocessing.dummy import Pool as ThreadPool
    from multiprocessing import cpu_count
    cnt_cpu = cpu_count()
    cpus = 10*cnt_cpu #线程池大小
    pool = ThreadPool(cpus)
    _lstParam = range(0,10000)
    pool.map(aJob,_lstParam)
    pool.close()
    pool.join()
    print("multi thread job done")

################以下是多进程############################    
def runProc(name):
    """
    提供给多进程调用
    """
    import os
    print("child process %s(%s)"%(name,os.getpid()))
    
def multiProcess():
    """
    多进程
    """
    from multiprocessing import Pool
    from multiprocessing import cpu_count
    import os
    cpus = 1*cpu_count()
    lst_grp = range(0,100)
    p = Pool(cpus)
    for i in range(0,100):
        p.apply_async(runProc,args=(lst_grp[i],))
    p.close()
    p.join()
    print("multi process job done")

def oneProcess():
    """
    启动一个进程
    """
    from multiprocessing import Process
    import os
    p = Process(target=runProc,args=("processName",))
    print("one process will start")
    p.start()
    p.join()
    print("one process end")

if __name__ == "__main__":
    multiThread()#多线程
    multiProcess()#多进程
    oneProcess()#启动一个进程