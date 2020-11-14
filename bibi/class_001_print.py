# -*- coding: utf-8 -*-
# @Time     :2020/11/14 下午 6:27
# @Author   :yutq.test
# @Email    :646642124@qq.com
# @File     :class_001_print.py
# -*- coding: utf-8 -*-
# @Time     :2020/11/12 下午 7:47
# @Author   :yutq.test
# @Email    :646642124@qq.com
# @File     :class_001_type函数.py
print("---1---")  #print函数打印 默认换行
print("---2---")
#占位符：%d（数字） %s（字符串） %f（浮点数，小数） %%（两个百分号表示一个%）
#保留2位小数%.2f
#格式： print（"字符串信息 占位符" %（连接符） 变量或数据）
name = '嚣张'
age = '22'
high = 180.235
print('姓名：%s' % name,'年龄：%s' % age,'身高：%.2f' % high)
print('姓名：%s,年龄：%s,身高：%.2f' %(name,age,high))#格式化输出按照格式输出
a=1
b=2
c=3
print(a,b,c)
# print(a,b,c) 可以打印多个变量
# 字符串 str string
# 成对的单引号 双引号 以及三引号扩起来的内容都是字符串
c='10'
d="hello yutq.test"
e=""""10.00000"""
print(type(e))
#如果你的字符里面必须包含单引号 最外层用双引号
#如果你的字符里面必须包含双引号 最外层用单引号
x='"hello test"'
print(x)
a=1
a=4
print(a)# 取值最后一个变量
# type()函数小结：
# 1.可以查看变量或数据的类型
# 2.使用 type(变量名) 或 type(数据)
#运算符 算术运算符 + - * /除 //求商 % 取余运算 6%5 **幂
#注意 *遇到字符串，可以使用字符串重复指定的次数
print()
print(6%5)
#比较运算符 == > >= < <= !=不等于
#比较运算符长春会和后面的if条件判断一起使用

