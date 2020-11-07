# -*- coding: utf-8 -*-
# @Time     :2020/6/9 下午 8:23
# @Author   :yutq.test
# @Email    :646642124@qq.com
#列表 关键字list 符号 []
# 1：特征
# 1.1中括号括起来的数据都是元组  看类型 用 type
# 1.2空列表 t=[ ]
# 1.4列表里面可以包含各种类型的数据 整数，浮点数，字符串，布尔值 
#1.5 元素与元素之间是用逗号隔开的，看元素的长度 len
# 1.6取值方式：与字符串一样 根据索引取值  可以切片取值
t=[2,0.01,'1',True,(1,2,3,'hello') ]
print(type(t))
p=[]
print(type(p))
b=['1']
print(type(b))

g=[2,0.0089,'1',True,(1,2,3,'hello'),['python13','lemon','土豆','西红柿']]
# print(g[4][2])
# print(g[5][2])
# print(g[-1][-2])
# print(g[-1][-1])
# #切片
# #请把最后一个嵌套列表的索引为偶数的值打印出来
# print(g[-1][::2])
# #增加
# #1：加在尾部 列表名.append(value) 一次只能增加一个元素
# g.append('爱飞的鱼')
# g.append('向阳同学')
# print(g)
# #2：在指定的索引位置加元素 列表名.insert(i,value) 一次只能增加一个元素
# g.insert(0,'花果山来的同学')
# print(g)
#3.添加列表名  列表名.extend(第二个列表名) 合并列表
# a=['皮的要死的海绵','磐石','melody','ing','如意']
# t.extend(a)
# print(g+a)
#删除
# 1.删除最后一个元素 列表名.pop()
# g.pop()
# print(g)
#2：删除指定位置索引引用位置的一个元素 列表名.pop(i)
# g.pop(0)
# print(g)
# 列表可以删除吗 元组不可用删除 是绝对的吗？---他不是绝对的

# 修改 修改元素的值 重新赋值
g[-1][-1]='shadow'
print(g)

#字典 关键字dict dictionary 符号 {}
# 1：特征
# 1.1大括号括起来的数据都是字典  看类型 用 type
# 1.2空列表 t={ }
# 1.3列表里面可以包含各类类型的数据
# value 数据类型不限 整数 浮点数 字符串 布尔值true--1 false 元组 列表 字典
#key：value键值对 用逗号区分开来
# 1.4取值方式：与字符串/元组一样 根据索引取值  可以切片取值
#嵌套取值 怎么取  剥洋葱 一片一片往里面剥开
d={'name':'执着','hobby':'学习python','age':18,
   'score':{'en':120,'math':99.99,'ch':'A'},
    'friend':['bay max','小cc','如意'],
   'good_man':True}
# print(len(d))
# print(d['friend'][0])
#字典嵌套取值
print(d['score']['en'])
#1.5支持增删改查
#增加 d[key] key是不存在字典里面 就是新增
d['name']='悠悠'  #这样会代替'name':'执着'
print(d)
#删除：根据key去删除
d.pop('friend')
print(d)
#随机删除
# d.popitem()
# print(d)
print(d.keys()) #获取字典里面所有的key
print(d.values()) #获取字典的所有value