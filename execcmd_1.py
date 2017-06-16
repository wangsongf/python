#!/usr/bin/python
import MySQLdb
import string
import os, re
import sys
import time
import urllib
import commands
import logging

def startSrv():
    print("startSrv....")
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except Exception, e:
        sys.stderr.write("fork 1 fail")
        sys.exit(1)
    os.chdir("/")
    os.setsid()
    os.umask(0)

    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except Exception, e:
        sys.stderr.write("fork 2 fail")
        sys.exit(1)

    sys.stdout.flush()
    sys.stderr.flush()

def loadConfig():
    dbhost = ""
    dbport ="" 
    dbname = ""
    serverindex = ""

    f = open("./gameworld/GameWorld.txt", "r")
    list = f.readlines() 
    find = False
    for line in list:
        if line.find("SQL") >= 0:
            find = True
            continue
        if line.find("ServerIndex") >= 0:
            m = re.search(r"\d+", line)
            if m:
                serverindex = m.group(0)
                print serverindex
            else:
                print "error!!" + line
                exit(-1)

        if find:
            if line.find("Host") >= 0:
                m = re.search(r"\"[^\"]*\"", line)
                if m:
                    dbhost = m.group(0).replace("\"", "")
                    print dbhost
                else:
                    print "error!!" + line
                    exit(-1)
            if line.find("Port") >= 0:
                m = re.search(r"\d+", line)
                if m:
                    dbport = m.group(0)
                    print dbport
                else:
                    print "error!!" + line
                    exit(-1)
            if line.find("DBName") >= 0:
                m = re.search(r"\"[^\"]*\"", line)
                if m:
                    dbname = m.group(0).replace("\"", "")
                    print dbname
                else:
                    print "error!!" + line
                    exit(-1)
            
            if dbname != "" and dbport != "" and dbhost != "" and serverindex != "":
                break
    return dbhost, dbport, dbname,serverindex

def process(sid, cmdid, cmd, para1, para2,dir):
    print("recv:" + cmd)
    output = ""
    if cmd == "update":
        status, output = commands.getstatusoutput(dir+"/update.sh")
        #upate:download and unzip
        print(output)
    elif cmd == "stop":
        status, output = commands.getstatusoutput(dir+"/stop.sh " +para1  +" " + dir)
        #upate:download and unzip
        print(output)
    elif cmd == "start":
        status, output = commands.getstatusoutput(dir+"/start.sh " +para1 +" " +para2 + " " + dir)
        #upate:download and unzip
        print(output)
    elif cmd == "gfqr":
        status, output = commands.getstatusoutput(dir+"/gfqr.sh " +para1 + " " + dir)
        print(output)
    elif cmd == "qfqr":
        status, output = commands.getstatusoutput(dir+"/qfqr.sh " +para1 + " " + dir)
        print(output)
    elif cmd == "mysql":
        print dbhost
        status, output = commands.getstatusoutput(dir+"/mysql.sh " +dbhost +" " +dbport +" " +dbname +" "  +para1 + " " +para2 +" " + dir)
        print(output)


    #send result to web server
    
    outputlist = output.split("\n")
    llen = len(outputlist)
    if llen > 0:
        output = outputlist[llen - 1]
    output = urllib.quote(output)
    url = "http://10.204.190.127/sacallback.jsp?cmdid=%d&ret=%s&sid=%d" % (cmdid, output, sid)
    print(url)
    f = urllib.urlopen(url)
    s = f.read()
    # if s == None or s == "":
    #    print("jsp invalid")
    #    exit(-1)
        
    print("web result:", s)
    logging.info("%s web result:%s" %(url,s))
    f.close()

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(levelname)s] %(levelname)s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                filename=os.path.join(dir,'servercmd.log'),
                filemode='a')
    print dir
    logging.info(dir)
    startSrv()
    print "========================="
    print("startSrv success!")
    print "========================="
    
    os.chdir(os.path.realpath(dir))
    
    # load config
    dbhost, dbport, dbname,serverindex = loadConfig()

    #connect to mysql
    conn = MySQLdb.Connect(host=dbhost, user='root', passwd="hoolai12", port=string.atoi(dbport), db=dbname)
    print("connect to mysql succ!")

    cur = conn.cursor()
    while True:
        # load cmd from db per 5 sec
        try:
            cur.execute("select id,serverid,cmdid, cmd, param1, param2 from servercmd where serverid=%s limit 1" % serverindex)
            if cur.rowcount >= 1:
                row = cur.fetchone()
                id = row[0]
                sid = row[1]
                process(sid, row[2], row[3], row[4], row[5],dir)
                            
                #after process cmd, should delete from db
                n = cur.execute("delete from servercmd where id=%d and serverid=%s" % (id,serverindex))
                logging.info("delete from servercmd where id=%d and serverid=%s result:%s" % (id,serverindex,n))
                if n <= 0:
                    exit(-1)    #delete error,exit system
            time.sleep(5)
        except MySQLdb.Error, e:
            logging.ERROR(str(e))
