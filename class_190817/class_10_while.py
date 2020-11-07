# -*- coding: utf-8 -*-
# @Time     :2020/7/9 下午 7:51
# @Author   :yutq.test
# @Email    :646642124@qq.com
# @File     :class_10_while.py
#循环
#函数的定义：实现某个指定的功能 重复使用
# type() 判断数据类型
# len()  统计数据元素长度
# range() 创建一个整数列表
#函数的作用:提高代码的复用性
#函数的语法：关键 def
#函数的具体语法：
#def 函数名（参数1，参数2，参数3）：
#函数体：本函数要实现的功能
#return 表达式
#def 顶格写 表示这个是一个函数
# 函数名 小写 不同的字母与数字之间用下划线隔开 不能用数字开头
#参数的个数可以大于等于0
#函数体是函数的子代码 要有缩进 写自己想实现的功能即可
#return后面的表达式 >=0个
#return 的作用就是你调用函数的时候 会返回return后面的表达式的值

#如何调用函数 函数名（对应个数的参数）
#None 没有返回任何的东西 空的
# def radio_machine():
#     print('就是一个复读机，只会说：你好！！！')
#     return 1+2 #隐式的添加一个return
# res=radio_machine()#存储返回的值
# print('函数的返回值是：{}'.format(res))
#函数里面return的表达式个数
#==1返回你指定的数据类型
#>1 返回的是元组类型，用逗号，区分
#==0 返回None

# def add():
#     result=8+8
#     print(result)
#     return result #8+8=16
# a=add()+20 #16+20=36
# print(a)

def count_nummber():
    count=0
    for i in range(1,100):
        count+=i
    print('计算结果是：{}'.format(count))
    return ##return后面的代码不再执行，所以我们的有效代码要放在return前面,return表示函数的结束
print(count_nummber())