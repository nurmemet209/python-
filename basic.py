
 
 # 这是单行注释

"""
这是多
行注释
"""

#一个空行表示一个代码块的结束，比如函数，类
#代码块用一致的缩进表示，比如下面到pring(454454) 是函数test的部分，空行表示test函数结束
#函数所有的行的缩进必须一致，不然报错
#函数必须先定义，才能调用
def test(a):
 print(a)
 print(45454)

def  test2():
    print("nurmemet")
    print("alim")

test(4)
test2()

#下面是for循环的例子
a=[1,2,3] #a是一个数组
for item in a:
    print(item)
    print("这部分也是属于for循环")

#下面是 in 和 not in 的使用
b=[1,2,3,4]
c=1
if c in b:
    print("这是in 的用法")
elif(c not in b):
    print("这是elif的用法")
else:
    print("这是else 的用法")


#下面是is 的用法
f=c
if f is c:
    print("这是is的用法")

#下面是del的用法,下面语句删除a，再往下使用a会报错
# 可以同时删除多个变量 del  a,b,c
a=100
del a
# print(a)

#数字类型转换
x=1.0
print(int(x))
x=11
print(float(x)) #会输出11.0

#不同的类型进行混合运算
a=3 * 3.75 / 1.5 #a 会变成浮点数
print(a)

#计算幂
print(5**2) #5的平方

#数学函数
import math
a=abs(-100) #取绝对值,abs是系统函数不需要math
print(a)
b=math.ceil(4.1)
print(b) #向上取整,输出5
a=math.exp(2) #e 的2次幂
print(a)
a=math.floor(4.9) #向下取整输出4
print(a)
a=math.log(100,10) #数学函数,输出2.0
print(a) 
print(max(1,2,2,3,4,511)) #返回最大的一个，参数个数不限制,系统函数
print(min(1,2,2,3,4,511)) #返回最小的一个，参数个数不限制,系统函数
print(math.modf(5.1232)) #返回整数部分与小数部分  输出(0.12319999999999975, 5.0)
print(pow(2,3)) #2的三次方，输出8
print ("round(56.659,1) : ", round(56.659,1)) #求四舍五入，后面的1是要保留的位数
print(math.sqrt(16)) #返回16的平方根 4.0



""" 下面是python3相关的内容 """

#Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如
total = "item_one" + \
        "item_two" + \
        "item_three"
print(total)

#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total)

#同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')  #输出runoob+一个空行

#多条语句赋值
a=b=c=1
print(a,b,c) #输出1,1,1
a,b,c=1,2,3
print(a,b,c) #输出1,2,3

#数据类型
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d)) #输出 <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

print(5 + 4)  # 加法
print(4.3 - 2) #减法
print(3 * 7) #乘法
print(2 / 4) #除法 得到一个浮点数 输出0.5
print(2 // 4) #除法 得到一个整数 输出0
print(17 % 3) #取余
print( 2 ** 5) #乘方

#字符串
str = 'Runoob'
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次
print (str + "TEST") # 连接字符串

#转移字符以及输出原始字符
print("nurmemet \n alim") #输出 nurmemet 空行  alim
print(r"nurmemet \n alim") #输出  nurmemet \n alim  ,这里不输出空行

#列表
#修改数组元素是非法的，但列表的元素是可以修改的
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

#Tuple（元组）
#与数组一样Tuple元素是不可修改的
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

#Set（集合）
#集合（set）是一个无序不重复元素的序列
#可以使用大括号({})或者 set()函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
student = ({'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'})
print(student)   # 输出集合，重复的元素被自动去掉
# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素

#Dictionary（字典）
#字典类型也有一些内置的函数，例如clear()、keys()、values()
#字典的关键字必须为不可变类型，且不能重复
#创建空字典使用 { }
dictT = {}
dictT['one'] = "1 - 菜鸟教程"
dictT[2]     = "2 - 菜鸟工具"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print (dictT['one'])       # 输出键为 'one' 的值
print (dictT[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值



#Python数据类型转换

#Python成员运算符
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")

if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if ( a in list ):
   print ("3 - 变量 a 在给定的列表中 list 中")
else:
   print ("3 - 变量 a 不在给定的列表中 list 中")


#Python身份运算符
a = 20
b = 20
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")

if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")

if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")

#Python字符串格式化
print ("我叫 %s 今年 %d 岁!" % ('小明', 10)) 

#Python三引号
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

#Python3 迭代器与生成器
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

import sys         # 引入 sys 模块



#python 都是引用传递
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print ("函数外取值: ", mylist)

#函数默认参数
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name);
   print ("年龄: ", age);
   return;
 
#调用printinfo函数
printinfo( age=50, name="runoob" );
print ("------------------------")
printinfo( name="runoob" );

#不定长参数
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;
 
# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );

#匿名函数
sum = lambda arg1, arg2: arg1 + arg2;
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))


#全局变量和局部变量
total = 0; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2; # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total;

#调用sum函数
sum( 10, 20 );
print ("函数外是全局变量 : ", total)

#列表推导式
vec = [2, 4, 6]
a=[3*x for x in vec] #生成新的列表
print(a) #输出[6, 12, 18]
b=[[x, x**2] for x in vec]
print(b) #[[2, 4], [4, 16], [6, 36]]

#嵌套列表解析
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],]
c=[[row[i] for row in matrix] for i in range(4)]
print(c) #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

#集合也有推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) #{'r', 'd'}


#字典的构造
print(dict(sape=4139, guido=4127, jack=4098)) #{'jack': 4098, 'sape': 4139, 'guido': 4127}
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])) #{'jack': 4098, 'sape': 4139, 'guido': 4127}
print({x: x**2 for x in (2, 4, 6)}) #{2: 4, 4: 16, 6: 36}

#字典的遍历
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
#输出 robin the brave
#gallahad the pure
for k, v in knights.items():  
     print(k, v)


#导入模块儿
import support
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")

#部分导入模块儿
from part_support import function1
function1("hello")
#要导入模块儿的全部函数可以用星号代替
from full_support import *
function2()

#菜鸟教程网址： "www.runoob.com!"
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com')) 
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob',other='Taobao'))
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi)) #保留小数点三位   常量 PI 的值近似为 3.142。

#键盘输入
str = input("请输入："); #这里会等待你输入，输入完之后按回车
print ("你输入的内容是: ", str)


#python 对象持久化到文件，并读取
import pickle
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()



import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

#异常处理
while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again   ")



#类
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

# 实例化类
p = people('runoob',10,30)
p.speak()

#json 转 list
import json
def json2list(jsonData):
    return json.loads(data)

#list 转 json
def  list2json(list):
    return json.dumps(list)