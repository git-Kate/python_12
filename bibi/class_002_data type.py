# -*- coding: utf-8 -*-
# @Time     :2020/11/15 上午 11:42
# @Author   :yutq.test
# @Email    :646642124@qq.com
# @File     :class_002_data type.py
'''
数字类型
整型 int
浮点型 float
布尔型 bool True——>1 fals-->0
复数型（听过即可）
非数字类型
字符串 str
列表 list
元组 tuple
字典 dict
'''
a = True + 10 #布尔类型参与运算时True当做整数1
print(a) #11
a = False + 10#布尔类型参与运算时False当做整数0
print(a) #10
# type()函数小结：
# 1.可以查看变量或数据的类型
# 2.使用 type(变量名) 或 type(数据)
print(type(a))
print(type(100))
'''
python中变量的数据类型是自动类型推导：
根据等号右边的数据类型
自动推导等号左边变量中保存的数据类型
'''
# 字符串 str 主要处理文本数据
# 打印原生字符串 加r a = r"I\'M itcastYY"
# 成对的双引号可以嵌套成对的单引号  "123‘445’678"
# 成对的单引号可以嵌套成对的双引号  ' " " '
# 字符串定义细节:
# 单引号字符串
# 双引号字符串
# 三引号字符串
# 特殊符号处理
'''
字符串的输入与输出:
输入：使用input()
作用获取用户的输入信息
注意:input(提示信息)函数获取的信息一般保存到变量中
注意:input(提示信息)获取的信息都是字符串类型
说明:input(提示信息)
输出:使用print(提示信息)默认是阻塞的，除非用户输入信息或关闭程序
'''
# user = input('请输入用户名：')#input(提示信息)一定要加提示信息
# print(user)
# print(type(user))
# print("-" * 50) #打印50个 -
# pwd = input('请输入密码：')
# print(pwd)
# print(type(pwd))
'''
字符串
查询字符串
索引就是字符在字符串中位置下标默认从0开始
1.根据索引查询字符中的数据
2.根据字符串中数据获取索引（通过数据获取索引）
3.不能超过字符串的索引值 越界报错
'''
#1.根据索引查询字符中的数据
my_str = 'hello,python'
print(my_str[0])# 打印结果 p
print(my_str[5])
#3.不能超过字符串的索引值 越界报错
#print(my_str[15])#越界报错IndexError: string index out of range
#2.根据字符串中数据获取索引（通过数据获取索引）
#格式：字符串名.index(数据值)
print(my_str.index('e'))
print(my_str.index('python'))#获取最左边的字符串索引
#统计字符串
# 1.统计字符串长度
#格式：len(字符串)
my_str1 = "hello,python,hello"
print(len(my_str1))
#统计大字符串中某个字符串出现的次数
#格式：大字符串名.count(小字符串)
#说明:字符串是一种有序的容器（字符串中数据是有顺序的，可以通过索引访问）
print(my_str1.count('l'))
print(my_str1.count('hello'))
#目标：字符串的查找与替换
#判断：
# 变量名.startswith('h') 检测字符串是否是以h开头，是则返回 True 不是则返回False
print(my_str1.startswith('h'))
# 变量名.endswith('o') 检测字符串是否是以o结尾，是则返回 True 不是则返回False
print(my_str1.endswith('o'))
#应用：查找以.py结尾的文件或者.html结尾的文件
info_str1 = "jd_20201116_goods_table.py"
info_str2 = "jd_20201116_goods_table.html"
print(info_str1.endswith('.py'))#endswith('.py')结尾
print(info_str1.startswith('jd'))#startswith('jd')开始
#查找 find
#在指定范围内查找，如果查询到了返回查询数据的索引值 否则返回 -1
my_str1 = "hello,python,hello"
print(my_str1.find('e'))#找到返回索引
print(my_str1.find('hello'))#返回最左边的第一个字符串的索引
print(my_str1.find('hello',8))#指定开始的范围 从8索引向后找
print(my_str1.find('hello',8,len(my_str1)))#指定范围查找
print(my_str1.find('java'))#没有找到返回-1 下面的代码正常执行
print(my_str1.find('o'))


