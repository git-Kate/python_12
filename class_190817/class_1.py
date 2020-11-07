#python解释器从上到下执行从右到左执行，先计算等号右边的值，赋值给等号左边的变量
# 标识符 --取名字  ，你来命名多的都叫标识符
# 标识符的规范
# 数字 字母 下划线 组成
# 不能以数字开头
# 字母和数字之间可以用下划线隔开 方便阅读
# 见名只意
# 不能以关键字命名
# #['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
import keyword
print(keyword.kwlist)

# class_1129_base

# 注释  单行  多行注释 成对的三引号 ''' , """
# 缩进 控制
# a=10
# if a==1:
#     print ('a的值为1')
# else:
#     print ('a的值不为1')
# print ('hello word !') #函数 输出内容到控制台
# a=input('请输入一个数据') #函数 从控制台获取数据
# print(a)

#获取文件路径 D:\PyCharm Community Edition 2017.2.3\python12\class_190817\class_1.py

# 变量名：命名一个标识符存储一个数据 变量名
#变量第一次出现叫定义，下次再出变量叫使用这个变量
#数字  字符串 列表 元祖 字典 集合 等各种类型的数据
# a=1
# b=1
# print(id(a))
# print(id(b))

# a=1
# b=2
# print(a)

#数字 ：证型，浮点型
# int 整型(有符号整型)
a=10
a=100
# 帮你判断数据类型的函数 type（数据）
print(type(a))
# 浮点型 float  引号不在就是浮点型
a=10.0
print(type(a))
# 字符串 str string
# 成对的单引号 双引号 以及三引号扩起来的内容都是字符串
c='10'
d="hello yutq.test"
e=""""10.00000"""
print(type(e))
##如果你的字符里面必须包含单引号 最外层用双引号
##如果你的字符里面必须包含双引号 最外层用单引号
x='"hello test"'
print(x)
a=1
a=4
print(a)# 取值最后一个变量


# type()函数小结：
# 1.可以查看变量或数据的类型
# 2.使用 type(变量名) 或 type(数据)




















