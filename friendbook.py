#!/usr/bin/python
#Filename:friendbook.py
import json as p
import sys
import time
import os
ab={'Xdex':'cneds@fnedf.com',
        'Laexly':'fev@fe.com',
        'Fukc':'fexok@ver.com',
        'Stifu':'stif@qq.com'
}

def Dumpfile(list):
        f=open('friendab.json','w')
        p.dump(list,f)
        f.close()

if os.path.isfile('friendab.json'):
        friendab='friendab.json'
else:
        os.system('touch friendab.json')
        Dumpfile(ab)
        del ab

with open('friendab.json') as f_obj:
    frilist = p.load(f_obj)

class Person:
        def __init__(self,name):
                self.name=name
        def saysome(self):
                print('The friend %s,his E-mail is %s '%(sname,frilist[sname]))
class addPerson:
        def __init__(self,name,email):
                self.name=name
                self.email=email
        def addbook(self):
                ab=frilist
                ab[sname]=email
                Dumpfile(ab)
                del ab
                print('Succlessful!')
class delPerson:
        def __init__(self,name):
                self.name=name
        def delbook(self):
                ab=frilist
                ab.pop(sname)
                Dumpfile(ab)
                del ab
                print('Success DEL')
class alterPerson:
        def __init__(self,name,email):
                self.name=name
                self.email=email
        def alterbook(self):
                ab=frilist
                ab[sname]=email
                Dumpfile(ab)
                del ab
                print('Succlessful update!')
print('''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
[1] : Search your friend's email from friendsbook
[2] : add your friend's email to firendsbook
[3] : del your friend's email from firnedsbook
[4] : alter your friend's email from friendsbook
[5] : All friends list
[6] : exit the program
''')

num=input('Press the number [1,2,3,4,5] -->')

if (num=='1'):
        sname=input('Enter the name-->')
        if sname in  frilist:
                p=Person(sname)
                p.saysome()
        else:
                print('Not in it')
elif (num=='2'):
        sname=input('Enter the name-->')
        email=input('Enter the email-->')
        pa=addPerson(sname,email)
        pa.addbook()
        #p=Person(sname)
        #p.saysome()
        print(frilist)
elif (num=='3'):
        sname=input('Enter the name-->')
        pa=delPerson(sname)
        pa.delbook()
elif (num=='4'):
        sname=input('Enter the name-->')
        if sname in  frilist:
                email=input('Enter the email-->')
                p=alterPerson(sname,email)
                p.alterbook()
        else:
                print('Not in it')
elif (num=='5'):
        print(frilist)
elif (num=='6'):
        print("Bye!")
else:
        print("Please input the right number")