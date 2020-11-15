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
input(提示信息)获取的信息都是字符串类型
输出：使用print()
'''
user = input('请输入用户名：')#input(提示信息)一定要加提示信息
print(user)
print(type(user))
print("-" * 50) #打印50个 -
pwd = input('请输入密码：')
print(pwd)
print(type(pwd))

