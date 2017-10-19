#coding: utf-8
# -*- coding:utf-8 -*-
input_name = input("Please input your user name : ").strip()
print(input_name)
exit(1)
user_lockfile = open("user_lockfile.txt","r+")
user_file = open("user_file.txt")
user_list = user_file.readlines()


for i in range(3):
    input_passwd = input("Please input your password : ").strip()
    #查找被锁用户列表判断是否被锁住
    if input_name in [locked_user.rstrip() for locked_user in user_lockfile.readlines()]:
        print("Sorry, your account is locked!")
        user_file.close()
        user_lockfile.close()
        exit(1)
    else: #没有被锁住，查找用户列表
        if input_name not in [user_record.split()[0] for user_record in user_list]:
            print("Sorry, your account doesn't exist!")
            user_file.close()
            user_lockfile.close()
            exit(2)
        else: #用户存在，判断密码是否正确，正确跳出循环
            input_record = input_name + ' ' + input_passwd
#            print(input_record)
#            print(user_file.tell()) #记录当前游标位置
            if input_record in [user_record.rstrip() for user_record in user_list]:
                print("Logging in...")
                user_file.close()
                user_lockfile.close()
                exit(0)
            else:#密码不正确，判断错误次数，错误三次（i=2）将用户锁住
                if i == 2:
                    user_lockfile.write(input_name + "\n")
                    print("Sorry, you're locked!")
                    user_file.close()
                    user_lockfile.close()
                    exit(3)
                else:#剩余机会数 2-i
                    chance = 2 - i
                    print("Wrong password! %s chances left!" % chance)
