
# -*- coding:utf-8 -*-
import time
import os

DICT_PRO = {"北京":["大兴区","朝阳区","海淀区","东城区","西城区","丰台区","通州区"],
            "上海":["静安区","徐汇区","浦东新区","虹口区","普陀区","长宁区","宝山区","嘉定区","闵行区"],
            "山东省":["烟台市","济南市","青岛市"],
            "辽宁省":["大连市","沈阳市"],
            "香港":None,
            "澳门":None,
            "台湾":["台北市"]}
DICT_CIT = {"烟台市":["莱山区","芝罘区","福山区","龙口市"],
            "青岛市":["李沧区","台东区","崂山区"],
            "济南市":["市中区","天桥区","历城区"],
            "大连市":["中山区","甘井子区","沙河口区","高新园区"],
            "沈阳市":["皇姑区","大东区","和平区","铁西区"]}

#将输入的数字转化成整数形式
def input_verify(choice):
    if str.isdigit(choice):
        choice = int(choice)
    return choice

#输出框架
def framework_show(province='', city='', district=''):
    os.system('cls')   #清屏
    print('''
######################################################
*                                                    *
*          欢迎进入省市区查询系统                    *
*                                                    *
######################################################
*                                                    *
*          省份 : %s  城市 : %s  区 : %s
*                                                    *
######################################################
    ''' % (province, city, district))

#展示欢迎界面
def welcome_show(province='', city='', district=''):
    print('''
######################################################
*                                                    *
*            Welcome to %s %s %s
*                                                    *
######################################################
    ''' % (province, city, district))

#从省份字典，提取省份以及直辖市展示
def province_show():
    global DICT_PRO
    global P_NAME
    global C_NAME
    global D_NAME
    global C_FLAG

    province_dict = {}
    #遍历省份字典，提取省份并添加编号输出展示
    for (n, p) in enumerate(DICT_PRO, 1):
        province_dict[n] = p
        #print('%d.%s' % (n, p) + '\t', end='')
        if(n % 4 == 0):
            print()
    print('\n================================================================')
    print('q : Exit')
    province_input = input('请输入省份编号或省份名称 : ')
    province_input = input_verify(province_input)
    if province_input == 'q':
        exit(0)
    elif province_input in province_dict.keys(): #输入的是数字编号，对全局省份赋值
        P_NAME = province_dict[province_input]
    elif province_input in province_dict.values():#输入的是省份名称
        P_NAME = province_input
    else:
        P_NAME = ''    #其他输入，提示输入错误
        print("Wrong Input!")
        time.sleep(2)

    while P_NAME:
        framework_show(P_NAME, C_NAME, D_NAME)  #调用框架
        if type(DICT_PRO[P_NAME]) is list:  #若省份后有城市列表，调用城市展示函数
            city_show(P_NAME)
            if C_FLAG == 'b':
                break
        else:  #若省份后无城市，直接调用展示函数
            welcome_show(P_NAME)
            time.sleep(5)
            P_NAME = ''
            break


#传入省份，展示城市列表
def city_show(province):
    global DICT_PRO
    global DICT_CIT
    global P_NAME
    global C_NAME
    global D_NAME
    global C_FLAG
    global D_FLAG

    city_list = DICT_PRO[province]
    city_dict = {}
    for (n, c) in enumerate(city_list, 1):
        city_dict[n] = c
        #print('%d.%s' % (n, c) + '\t', end='')
        if (n % 4 == 0):
            print()
    print('\n================================================================')
    print('q : Exit    b : Back')
    city_input = input('请输入城市编号或城市名称:')
    city_input = input_verify(city_input)

    if city_input == 'q':
        exit(0)
    elif city_input == 'b':
        (P_NAME, C_NAME, C_FLAG) = ('', '', 'b')
        return
    elif city_input in city_dict.keys():
        city_name = city_dict[city_input]
        (P_NAME, C_NAME, C_FLAG) = (province, city_name, '')
    elif city_input in city_dict.values():
        city_name = city_input
        (P_NAME, C_NAME, C_FLAG) = (province, city_name, '')
    else:
        print("Wrong Input!")
        C_NAME = ''
        time.sleep(2)

    while C_NAME:
        framework_show(P_NAME, C_NAME, D_NAME)
        if C_NAME in DICT_CIT.keys():  #若所选城市在城市及区字典中有记录
            district_show(P_NAME, C_NAME) #调用城区展示函数展示城区
            if D_FLAG == 'b':
                break
        else:
            welcome_show(P_NAME, C_NAME)  #若所选城市在城区字典中无记录，调用展示函数
            time.sleep(5)
            C_NAME = ''  #展示后将城市清空，回到选择城市界面
            break



#传入省份和城市，展示相关地区
def district_show(province, city):
    global DICT_PRO
    global DICT_CIT
    global P_NAME
    global C_NAME
    global D_NAME
    global D_FLAG

    district_dict = {}
    district_list = DICT_CIT[city]
    for (n, d) in enumerate(district_list, 1):
        district_dict[n] = d
        #print('%d.%s' % (n, d) + '\t', end='')
        if (n % 4 == 0):
            print()
    print('\n================================================================')
    print('q : Exit    b : Back')

    district_input = input('请输入区名或编号:')
    district_input = input_verify(district_input)

    if district_input == 'q':
        exit(0)
    elif district_input == 'b':
        (P_NAME, C_NAME, D_NAME, D_FLAG) = (province, '', '', 'b')
        return
    elif district_input in district_dict.keys():
        district_name = district_dict[district_input]
        (P_NAME, C_NAME, D_NAME, D_FLAG) = (province, city, district_name,'')
    elif district_input in district_dict.values():
        district_name = district_input
        (P_NAME, C_NAME, D_NAME, D_FLAG) = (province, city, district_name,'')
    else:
        (P_NAME, C_NAME, D_NAME, D_FLAG) = (province, city, '', '')
        district_name = ''
        print("Wrong Input!")
        time.sleep(2)

    if district_name:      #若选中了城区，调用展示函数
        welcome_show(P_NAME, C_NAME, D_NAME)
        time.sleep(5)
        D_NAME = ''  #展示后将城区清空，将回到城区选择界面


P_NAME=''   #省份全局变量
C_NAME=''   #城市全局变量
D_NAME=''   #城区全局变量
C_FLAG=''   #城市选择页面输入b选项
D_FLAG=''   #城区选择页面输入b选项


while True:
    framework_show(P_NAME, C_NAME, D_NAME)
    province_show()
