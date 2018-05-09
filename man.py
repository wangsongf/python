#! /usr/bin/python
#coding:UTF-8
'''
    @author: neptune
    @time: 2014-02-20
    @descript: 主要记录Pyhon中一些常用的东西.建议宽屏阅读使用
'''
import sys
import re

def demo_help():
    print "快速查找:利用编辑的查找功能查找@关键字。"
    print "\t例如：查找list相关的东西：输入@list"
    print "\t查看运行结果:shell$ ./man.py list"
    print "输入./man.py -m list 可以查看list的API帮助"
    print "输入./man.py base 可以查看基础的数据类型列表"
    print "输入./man.py convert 可以查看类型转换函数"
    
def demo_api(datatype,spacing=15,collapse=1):
    """Print methods and doc-strings wtih object"""

    methodList = [method for method in dir(datatype) if callable(getattr(datatype,method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)

    print "\n".join(["%s %s" % 
        (method.ljust(spacing),processFunc(str(getattr(datatype,method).__doc__)))
        for method in methodList]);

#===========================================================================================================
#@list
#    演示list相关的用法
#===========================================================================================================
def demo_list():
    "演示list相关的用法"
    print "list类型：属于一种集合类型，它非常灵活，支持在源处修改，可按需增长缩短，可以包含任何类型的对象亦可嵌套"
    
    #define list variable 定义list类型的变量
    li1 = [];
    li2 = [1,2,3,4,5]   
    li3 = [1,2,3,'4',5]
    li4 = [1,'snakeam',['am','pm'],'fun']
    li5 = list("list-variable")
    li6 = list(range(-4,4))
    print "li1:",type(li1),"+\t",li1
    print "li2:",type(li1),"+\t",li2
    print "li3:",type(li1),"+\t",li3
    print "li4:",type(li1),"+\t",li4
    print "li5:",type(li1),"+\t",li5
    print "li6:",type(li1),"+\t",li6
    
    #index  form 0-index
    print li2[0]
    print li3[3]
    print li4[1][1]
    
    #split
    print li2[:3]       #取前三个元素，返回list
    print li3[3:]       #取第三个以后的元素，返回list
    print li3[2:4]      #从第三个开始取到第五个但不包括5
    print li3[-1:]      #取最后一个
    
    #add or del
    li1.append("hello")
    print li1
    li1.insert(0, "xcx")
    print li1
    li1[0:0] =['hmj']
    print li1
    li1[1:1] =['zxy']
    print li1
    li1[len(li1):1]=['world']
    print li1
    li1[-1] =['!','wan an']
    print li1
    
    del li1[0]
    print li1
    li1.remove(li1[0])
    print li1
    li1[2][0:1]=['I']
    print li1
    li1.pop()
    print li1
    
    #len
    print "li1's length",len(li1)
    
    #iterator
    listdemo = [x** 2 for x in li2]
    print listdemo
    
    
    for x in li2:print x*2
    #filter element : if expresstion
    li = [x *2 for x in li1 if x > 2]
    print li
    #
    #         list的方法
    #         L.append(var) #追加元素
    #         L.insert(index,var)
    #         L.pop(var) #返回最后一个元素，并从list中删除之
    #         L.remove(var) #删除第一次出现的该元素
    #         L.count(var) #该元素在列表中出现的个数
    #         L.index(var) #该元素的位置,无则抛异常
    #         L.extend(list) #追加list，即合并list到L上
    #         L.sort() #排序
    #         L.reverse() #倒序
    #         list 操作符:,+,*，关键字del
    #         a[1:] #片段操作符，用于子list的提取
    #         [1,2]+[3,4] #为[1,2,3,4]。同extend()
    #         [2]*4 #为[2,2,2,2]
    #         del L[1] #删除指定下标的元素
    #         del L[1:3] #删除指定下标范围的元素
    #         list的复制
    #         L1 = L #L1为L的别名，用C来说就是指针地址相同，对L1操作即对L操作。函数参数就是这样传递的
    #         L1 = L[:] #L1为L的克隆，即另一个拷贝。
#===========================================================================================================
#@dict
#    演示dict相关的用法
#===========================================================================================================
def demo_dict():
    """演示dict的常用操作"""
    #静态的创建一个字典
    d1 = {}                                      #创建一个空字典
    print d1
    d2 = {'name':'snakeam','skill':'decode'}     #创建有俩想的字典
    print d2
    d3 = {'food':{'ham':1,'egg':2}}              #字典的嵌套
    #Python 3.x
    #d4 = dict(name='xcx',skill='god'）
    print d3
    # print d4
    #动态构造一个字典
    #在Python3.x和Python2.x中字典可以用字典解析来创建。
    #字典解析运行一个隐士循环，根据每次迭代的收集表达式键/值结果来填充一个新的字典
    #动态初始化一个字典的标准方法都是：将其键和值对应起来传递个dict调用
    #zip函数是在一个单个调用中从键和值的列表来构建一个字典的方式之一
    li =['a','b','c']
    li2 =[1,2,3,4]
    d5 = dict(zip(li,li2))
    print d5
    
    #演示dict字典的取值
    print d2['name']
    print d3['food']['egg']
    #dict.get(key,0) 如果没有则返回默认值，[key]方式没有则抛出异常
    print d2.get('age',100)
    
    #成员关系：键是否存在测试
    print ('ham' in d3)
    #has_key(key)判断字典是否包含莫个键
    print d2.has_key('age')
    
    
    #Python2.x
    list_key = d5.keys()
    print "type=>",type(list_key)       #list
    print list_key                      #['a','b','c']
    
    list_value = d5.values()
    print "type=>",type(list_value)     #list
    print list_value                    #[1,2,3]
    
    list_item = d5.items()
    print "type=>",type(list_item)      #list
    print list_item                     #[('a',1),('b',2),('c',3)]
    #python3.x
    #keys,values,items都返回试图对象，而不向Python2.x中返回实际的结果集列表
    #视图对象是可迭代。这就意味着每次产生一个结果集项，而不是在内存中直接生存列表
    #视图保存了字典的最初顺，但他们不支持索引和列表的sort等方法。打印时也不现实自己的项
    
    #add  mondify
    d2['age']=100                   #为d2新增{'age':100}
    print d2
    d2['age']=20                    #修改age
    print d2
    del d2['name']                  #删除name建值对
    print(d2.pop('age'))
    print(d2.popitem())
    #字典合并
    d1.update(d2)
    print d1
    
    #字典遍历
    print d5
    for (k,v) in d5.items(): print "%s:%s" % (k,v) 
    #最笨的方法 
    for d in d5: print "%s:%s" % (d,d5[d])
    for k,v in zip(d5.iterkeys(),d5.itervalues()): print "%s:%s" % (k,v)
    #for k,v in zip(d5.keys(),d5.values()): print "%s:%s" % (k,v)
    #效率最高的
    for k,v in d5.iteritems(): print "%s:%s" % (k,v)
    
#===========================================================================================================
#@tuple
#    演示元组的使用
#===========================================================================================================
def demo_tuple():
    """元组tuple。元组由简单的对象构成，元组与列表非常类似，但元组不能在原处修改，因为它是不可变的。而且通常写成
        园括号而不是方括号中的一系列项。元组不支持任何方法调用，但元组具有列表的大多数属性。
        任意对象的有序集合
            与字符串和列表类似，元组是一个位置有序的对象集合，与列表相同，可以嵌入到任何类别的对象中
        通过偏移存取
            同字符串，列表一样，在元组中的元素通过偏移来访问，它们支持所有基于偏移的操作。
        不可变序列类型
            类似于字符串，元组是不可变的。它们不支持应用在列表中任何原处修改的操作。
        固定长度，异构，任意嵌套
            元组因为是不可变的，在不生成一个拷贝的情况下不能增长或缩短。另一方面，元组可以包含其他的符号对象，
        对象引用的数组
            与列表相似，元组最好看做是对象引用的数组。元组存储指向其他对象的存储点
    """
    #定义元组
    ()                      #定义个空元组
    T = (0,)                #定义一个元素的元组，注意逗号不能少
    print T
    T = (1,'snake',2,3,4)
    print T
    T = 0,'ni',1,2,3
    print T
    T = ('snakeam',('java','c','web','asm'),'python')
    print T
    T1 = tuple("poseido")       #一个可迭代对象元组
    print T1
    
    #进行索引
    print T[1]
    print T[1][1]
    #分片
    print T[1:2]
    #合并
    print T+T1
    #重复
    print T *3
    #迭代
    for x in T:print x
    for x in T1:print x
    #成员关系
    print T.index('python')
    print T1.index('s')
    #计数
    print (T * 3).count('python')
    
    #tuple 和list相互转换
    li1 = list(T)
    print "type=>",type(li1),'\n',li1
    li1.sort()
    print li1
    T = tuple(li1)
    print "type=>",type(T),'\n',T
#===========================================================================================================
#@string
#    演示字符串的使用
#===========================================================================================================    
def demo_string():
    """
        Python中字符串的定义：一个有序的字符的集合，用来存储和表现基于文件的信息。
        Python中的字符串与其他语言中的字符串一样扮演着重要的角色。
        严格的说Python中字符串要算是不可变的序列这一类别。意味着这些字符从所包含的字符存在从左至右的顺序
        并且它们不可以在源处修改。
    """
    #下面是一些常用的字符串常量和表达式的定义
    S = ""              #空字符串
    print S
    S = "i'am chinese people!"  #双引号和单引号相同
    print S
    S = 's\np\ta\x00m'          #转意
    print S
    S = """
            可以包含多行字符串
        """
    print S
    S = r"\temp\span"           #Raw字符串
    print S
    S = b'spam'                 #Python中的字节字符串
    print S
    S = u"测试"               #2.x中使用的unicode字符串
    print S
    
    #字符串的一些常用操作
    print   S +"this's a String"    #字符串合并
    strs =   " xcx hmj zxy " *3        #重复3次
    print strs
    #索引
    print strs[1]
    #分片
    print strs[1:4]
    #求长度
    print len(strs)
    #字符从格式化表达式
    print "a %s skill" % "super"
    print "a {0} skill".format("super")
    
    #字符串搜索
    print strs.find("x")
    #移除空格
    print strs.strip()
    print strs.rstrip()
    print strs.lstrip()
    #用制定的字符进行分割
    li = strs.split(" ")
    print "li's type=>",type(li)
    print li
    print "内容测试：",strs.isdigit()
    print "大小写转换",strs.upper()
    print "是否是以制定的字符结尾",strs.endswith(" ")
    print "<|>".join(list("snakeam"))
    print strs.encode("latin-1")
    #成员关系
    print "xcx" in strs
    #迭代
    for x in strs:print x*2
    print [ord(x) for x in strs]
    """
        Python内置的字符串处理函数
        * 获取长度的函数
            len()
        * 字母大小写转换
            str.upper()        全部大写
            str.lower()        全部小写
            str.swapcase()     大小写转换
            str.capitalize()    首字母大写
            str.title()        首字母大写
        * 字符从搜索
            str.find('t')        搜索制定的字符从，没有返回-1
            str.find('t',start)    从指定的位置开始搜索字符从
            str.find('t',start,end)    在指定的区间进行搜索
            str.rfind('t')            从右边开始查找
            str.count('t')            搜索字符串并做统计
            str.index()
        *格式化
            str.rjust(witdh)        获取固定长度，右对其，左边不够用空格补齐
            str.ljust(witdh)        获取固定长度，左对其，右边不够用空格补齐
            str.center(witdh)        中间对其
            str.zfill(witdh)         右对其，左边不足用0补齐
        *去除空格及制定的字符
            str.strip()            去除两边的空格
            str.lstrip()            去除左边的空格
            str.rstrip()            去除右边的空格
            str.strip('d')            去除俩变字符从，有相应的lstrip()和rstrip()
        *切分
            str.split('分割符')    分割字符从
        *判断
            str.startswith('a')        是否以指定的字符串开头
            str.endswith('a')            是否以制定的字符串结尾
            str.isalnum()            判断是否全部为字母或数字
            str.isaplha()            判断师傅全为字母
            str.isdigit()            是否全为数字
            str.isupper()            是否全部为大写
            str.islower()            是否全部为小写
    """
#===========================================================================================================
#@number
#    演示数值的一些基本操作
#=========================================================================================================== 
def demo_number():
    docstr =  """
        x << y                  左移
        x >> y                  右移
        x & y                   按位与
        x | y                   按位或
        x ^ y                   按位异或 (exclusive or)
        ~x                      按位翻转
        x + y                   加
        x - y                   减
        x * y                   乘
        x / y                   常规除
        x // y                  地板除
        x ** y                  乘方 (xy )
        x % y                   取模 (x mod y )
        -x                      改变操作数的符号位
        +x                      什么也不做
        ~x                      ~x=-(x+1)
        abs(x )                 绝对值
        divmod(x ,y )           返回 (int(x / y ), x % y )
        pow(x ,y [,modulo ])    返回 (x ** y ) x % modulo
        round(x ,[n])           四舍五入，n为小数点位数
        x < y                   小于
        x > y                   大于
        x == y                  等于
        x != y                  不等于(与<>相同)
        x >= y                  大于等于
        x <= y                  小于等于
    """
    print docstr
#===========================================================================================================
#@base
#    演示数值的一些基本操作
#===========================================================================================================
def demo_base():
    print """在Python程序中处理的每样对象都是一种对象。在Python中没有类型声明，运行的表达式语法觉得了
    创建和使用的对象的类型。"""
    print "Python中内置的对象类型："
    print "---------------------------------------------------------------------------------"
    print "对象类型".ljust(20),"常量/创建".ljust
    print "数字".ljust(20),"123,3.133,Decimal,Fraction".ljust
    print "字符串".ljust(20),"this's string".ljust
    print "列表".ljust(20),"[1,[2,’three’],4]".ljust
    print "字典".ljust(20),"{‘food’:’spam’,’taste’:’yum’}".ljust
    print "元组".ljust(20),"(1,’spam’,4,’U’)".ljust
    print "文件".ljust(20),"Myfile=open(‘eggs’,’r’)".ljust
    print "集合".ljust(20),"set(‘abc’),{‘a’,’b’,’c’}".ljust
    print "其他类型".ljust(20),"类型,None,布尔类型".ljust
    print "编程单元类型".ljust(20),"函数，模块，类".ljust
    print "与实现相关的类型".ljust(20),"编译的代码堆栈跟踪".ljust
    print "---------------------------------------------------------------------------------"
#===========================================================================================================
#@convert
#    演示类型转换的一些基本操作
#===========================================================================================================
def demo_convert():
    print "一些类型转换函数"
    
    res_str ="""
        int(x [,base ])         将x转换为一个整数
        long(x [,base ])        将x转换为一个长整数
        float(x )               将x转换到一个浮点数
        complex(real [,imag ])  创建一个复数
        str(x )                 将对象 x 转换为字符串
        repr(x )                将对象 x 转换为表达式字符串
        eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
        tuple(s )               将序列 s 转换为一个元组
        list(s )                将序列 s 转换为一个列表
        chr(x )                 将一个整数转换为一个字符
        unichr(x )              将一个整数转换为Unicode字符
        ord(x )                 将一个字符转换为它的整数值
        hex(x )                 将一个整数转换为一个十六进制字符串
        oct(x )                 将一个整数转换为一个八进制字符串
        """
    print res_str
#===========================================================================================================
#@set
#    演示集合的一些基本操作
#===========================================================================================================
def demo_set():
    print """
        集合set是一些唯一的，不可变的对象的一个无序集合。这些对象支持与数学集合理论上想对应的操作
            一个项在集合中只能出现一次，不管将它添加了多少次
        """
    #创建集合
    #    python3.x
    #     set1 = {1}
    #     print "type=>",type(set1),set1
    #     #注意set2 ={} type(set2) 
    #     set2 ={}    #set2其实是字典
    #     print "type=>",type(set2),set2
    #以列表位基础创建集合
    list1 = list("sebug.net")
    set3 = set(list1)
    print "type=>",type(set3),set3
    
    print "修改集合"
    print "\t有俩中方法可以向现有的集合在添加值:add()和update()"
    set3.add(4)
    set3.add(4)
    print "len(set4)=>",len(set3),set3
    
    set5 = set(['html','body','form','input','script'])
    print "len(set5)=>",len(set5),set5
    set5.update(set(['div','select','option','textarea','label']))
    print "len(set5)=>",len(set5),set5
    
    print "\t有三种方法可以删除集合中的元素discard(),remove() pop()"
    set6 = set(range(10))
    print "len(set6)=>",len(set6),set6
    #discard()接收一个单值作为参数，并从集合中删除该值,如果该值不存在执行一个空操作
    set6.discard(8)
    print "len(set6)=>",len(set6),set6
    #remove()接收一个单值作为参数，并从集合中删除该值，如果改制不存在将抛出KeyError
    set6.remove(6)
    print "len(set6)=>",len(set6),set6
    #pop()从集合随机删除某个值，并返回该值
    print  set6.pop()
    print "len(set6)=>",len(set6),set6
    #clear()将集合清空
    set6.clear()
    print "len(set6)=>",len(set6),set6
    
    #成员测试
    set7 = set(range(20))
    print 15 in set7
    print 20 in set7
    print 30 not in set7
    
    #集合操作
    #union()    方法返回一个新集合，其中包括俩个集合中的所有元素
    #intersection()    返回一个的新的集合，其中包括俩个集合中同时出现的元素
    #difference()    返回新的几个，其中包前面集合有但后面集合没有的元素
    #symmetric_difference()    方法返回一个新的集合，其中装着所有只在一个中出现的元素
    set8 =set(range(4))
    set9 = set(range(8))
    set0 = set(range(20))
    print set8.union(set9)
    print set9.intersection(set8)
    print set0.difference(set9)
    print set0.symmetric_difference(set8)
    
    #集合包含操作issubset()/issuperset()
    print set8.issubset(set9)
    print set9.issuperset(set8)
    
    #布尔值环境下
    print "\t布尔值环境下：空集合位假，包含至少一个元素不论其值都位真"
    if set():
        print "这个一个空几个"
    else:
        print "集合不为空"
#===========================================================================================================
#@re
#    演示正则表达式的一些基本操作
#===========================================================================================================   
def demo_re():
    
    print """
        正则表达式是搜索，替换和解析复杂字符模式的一种强大的而标准的方法。几乎在所有语言中都可以使用其来处理字符串。
        在Python中通过re模块可以使用正则。通过re模块，提供了各种正则表达式的匹配操作，在文本解析，复杂字符串分析
        和信息提取时是非常有用的操作。
        re模块尽管不能满足所有复杂的匹配情况，但足够在绝大多数情况下能有有效的处理字符，python会将正则表达式转
        换位字节码，利用C语言的匹配引擎进行深度优先匹配
        下面是一些正则表达式的基本语法:
      
        "."            任意字符
        "^"            字符串开始
        "$"            字符串结尾
        "*"            0 个或多个字符（贪婪匹配）
        "+"            1 个或多个字符（贪婪匹配）
        "?"            0 个或多个字符（贪婪匹配）
        *?,+?,??       以上三个取第一个匹配结果（非贪婪匹配）
        {m,n}          对于前一个字符重复m到n次，{m}亦可a{6}匹配6个a、a{2,4}匹配2到4个a
        {m,n}?         对于前一个字符重复m到n次，并取尽可能少‘aaaaaa’中a{2,4}只会匹配2个
        "\\"           特殊字符转义或者特殊序列    
        []             表示一个字符集    [0-9]、[a-z]、[A-Z]、[^0]
        "|"            或    A|B,或运算
        (...)          匹配括号中任意表达式    
        (?#...)        注释，可忽略    
        (?=...)        Matches if ... matches next, '(?=test)'在hellotest中匹配hello
        (?!...)        Matches if ... doesn't match next.'(?!=test)'  若hello后面不为test，匹配hello
        (?<=...)       Matches if preceded by ... .'(?<=hello)test'  在hellotest中匹配test
        (?<!...)       Matches if not preceded by ....'(?<!hello)test'  在hellotest中不匹配test
        
        ^ 匹配字符串开始位置。
        $ 匹配字符串结束位置。
        \b 匹配一个单词边界。
        \d 匹配一个数字。
        \D 匹配一个任意的非数字字符。
        x? 匹配可选的x字符。换句话说，就是0个或者1个x字符。
        x* 匹配0个或更多的x。
        x+ 匹配1个或者更多x。
        x{n,m} 匹配n到m个x，至少n个，不能超过m个。
        (a|b|c) 匹配单独的任意一个a或者b或者c。
        (x) 这是一个组，它会记忆它匹配到的字符串。你可以用re.search返回的匹配对象的groups()函数来获取到匹配的值。
        """
    rl = re.compile(r"world")
    if rl.match('helloworld'):
        print 'match success!'
    else:
        print 'match faild!'
    if rl.search("helloworld"):
        print 'search success!'
    else:
        print 'search faild!'
    
    #直接调用
    if re.search(r'abc','hello abc world'):
        print 'search success!'
    else:
        print 'search faild!'
    
    strs = "192.168.1.1"
    li = re.split("\.",strs)
    print "type(li)=>",type(li),li
    strs = re.sub("\.","-",strs)
    print strs
    print re.subn("-",".",strs)
    
    rl = re.compile(r'\d')
    print re.findall(rl,"hello[h1]held3sds3iwonder]lo")
    
    #松散式的正则
    print """
        python允许使用松散式的正则表达式，松散式的正则表达式和普通的正则表达式有俩点不同：
            空白符被忽略！空格，制表符和回车符在表达式中并不会匹配，如果想让作用可以转意
            注释信息被忽略
    
    patterns ='''
        ^            #字符从开头
        M{0,3}       #一些注释
        (cx|cl)      #一些注释
        $
    '''
    re.search(patterns,'M',re.VERBOSE)  #额外的参数re.VERBOSE必须传
    """
#===========================================================================================================
#@file
#    演示文件的一些基本操作
#===========================================================================================================
def demo_file():
    print '''
        Python提供了通用的文件操作方式，主要涉及os和shutil俩个模块
    '''
    print """常用的API有：
    os.getcwd()    返回Python脚本当前的工作路径
    os.listdir()    返回制定目录下的所有文件和目录
    os.remove()    函数用来删除一个文件
    os.removedirs()    删除多个目录
    os.path.isfile()    校验给出的路径是否是一个文件
    os.path.isdir()    校验给出的路径是否是一个目录
    os.path.isabs()    判断是否是绝对路径
    os.path.exists()    校验给出的文件是否存在
    os.path.split()    返回路径的目录名和文件名 返回tule
    os.path.splitext()    分离扩展命
    os.path.dirname()    获取路径名
    os.path.basename()    获取文件名
    os.system()    运行shell命令
    os.getenv()/os.putenv()    读取和设置环境变量
    os.linesep    给出当前平台的换行符
    os.name    指示正在使用的平台
    os.rename(old,new)    重命名
    os.makedirs()    创建多级目录
    os.stat(file)    获取文件属性
    os.chmod(file)    修改文件权限于时间戳
    os.exit()    终止当前进程
    os.path.getsize()    获取文件大小
    os.mknod()    创建空文件
    os.redir()    删除空目录
    os.chdir()    换路径
    os.mkdir()    创建目录
    fp = open()    打开文件，类似于window中的获取文件的操作句柄
    fp.read([size])    以byte为单位读取数据
    fp.readline([size])    按行读取，如果有size可能返回的是一行的部分
    fp.readlines()    按行读取全部内容，以list的形式返回
    fp.write(str)    把str写到文件中，write()并不会在str后面加上换行符
    fp.writelines(seq)    把seq的内容全部写入到文件中(多行一次写入，不会添加换行符)
    fp.close()    关闭文件
    fp.flush()    把缓冲区的内容写入到硬盘
    fp.fileno()    返回一个长整形的文件标签
    fp.isatty()    文件是否是一个终端文件
    fp.tell()    返回文件操作标记的当前位置，以文件的开头原点
    fp.next()    返回下一行，并将文件操作标记移位到下一行
    fp.seek(offset,[whence])    将文件打操作标记移动到offset的位置
    fp.truncate([size])    把文件裁成指定大小
    shutil.copyfile()    复制文件
    shutil.copy()    复制文件，可以是目录
    shutil.copytree()    复制为新目录
    shutil.move()    移动文件
    shutil.rmtree()     删除目录
    """
#===========================================================================================================
#@html
#    Python和HTML
#===========================================================================================================
def demo_html():
    print "用Python处理和生成html文件及其方便。下面是一些常用的框架和模块"
    print "解析html可以使用HTMLParser/SGMLParser/PyQuery/BeautifulSoup"
    print "用于web开发可以使用Django/Uliweb/PyJS/Eurasia"
    print "具体实例请看./HTML"
#===========================================================================================================
if __name__ == "__main__":
    #print sys.argv
    if len(sys.argv) >=2:
        selfMod = __import__(__name__)
        if sys.argv[1] == '-m':
            return_function = getattr(selfMod,"demo_api")
            if(callable(selfMod.return_function)):
                return_function(sys.argv[2])
        else:
            return_function = getattr(selfMod,"demo_%s" % sys.argv[1])
            if(callable(selfMod.return_function)):
                return_function()
    else:
        demo_help()
