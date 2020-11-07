# -*- coding: utf-8 -*-
# @Time     :2020/6/16 下午 8:18
# @Author   :yutq.test
# @Email    :646642124@qq.com

#运算符课程
# 算术运算符 + - * / % 取余运算 6%5
# print(6%5)
#取余运算干啥？？判断一个数是奇数还是偶数
# 网上获取代码  判断一个数是奇数还是偶数
# while True:
#     try:
#         num=int(input('输入一个整数：')) #判断输入是否为整数
#     except ValueError: #不是纯数字需要重新输入
#         print("输入的不是整数！")
#         continue
#     if num%2==0:
#         print('偶数')
#     else:
#         print('奇数')
#     break
#赋值运算符 = += -=
# a=1    #1存在内存里面 a相当于1的引用
# a+=5 #a=a+1
# print(a)
# #比较运算符 == > >= < <= !=
#运算结果： 布尔值 true  False
# print(3==4)
# print(3!=4) #不等于
# print(3>4)
# print(3<4)
# print('get'=='GET')#大小写判断 字母区分大小写
# print('get'=='get')
# print(a>0 and b>0) # and 且 左右两边满足才为真
# print(a>0 or b>0) #or 或 左右两边只要有一边满足即可    not取否定
#成员运算符：in 包含 not in不包含  运算结果 布尔值 true  False
str_1='hello'
print('h' in str_1)
str_1='hello'
print('1' in str_1)
t=[1,'hello',666,9.09]
print('h' in t[1])
d={'name':'小cc','age':22}
print('name' in d) #只能取key值