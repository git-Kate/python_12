# -*- coding: utf-8 -*-
# @Time     :2020/6/20 下午 5:01
# @Author   :yutq.test
# @Email    :646642124@qq.com
# @File     :class_9_for.py
# for循环
# s='python13'
# L=[1,0.2,'桃子','旅行者','莉红']
# d={'name':'katt','age':18,'money':'10w'}
# t=(1,5,6,'hi','how are you')
#单曲循环 in 包含
# for item in s: #遍历 访问s 每访问一次就打印一次 利用for循环 依次访问s里面的每一个元素 赋值给item这个变量
#     print(item)
#     print('---')
# a=0
# for item in s:
#     a+=1
#     print('{0}我要唱 青藏高原！！！'.format(a))
#     print('---')
#遍历去控制循环次数 -循环次数由元素的长度决定
    #练习：for循环 依次打印d里面的value值
# for item in d.values():
#     print(item)
# p=[[1,2,3],[4,5,6],[7,8,9]]
# #请一次方位p里面的子列表里面的每个元素 并且打印出来
# for a in p:
#     for b in a:
#         print(b)

#for 循环作业：1.遍历元素 2.可以控制循环次数
#for 循环可用来遍历的数据类型：str tuple list dict --目前所学的
#只要是可迭代的 就可以用for循环来遍历
#可迭代的数据类型：数据里面允许存在多个元素
#整数int类型不可迭代
# d={'name':'katt','age':18,'money':'10w'}
# print(d.keys())
# print(d.values())
# print(type(d.keys()))
# print(iter(d.keys()))
# d={'name':'katt','age':18,'money':'10w'}
# a=0
# for item in d.values():
#     a+=1
#     print('这是第{}次循环'.format(a))
#     print(item)
#     print()#打印为空，换行作用
 #range函数：生成一个整数序列 可迭代的对象
 #range（m,n,k）开头的数字 n结尾的数据 k步长，默认值为1 取左不取右
#如果range(m,n)k默认为 1
#如果range(n)m默认为 0
# res=range(1,10,3)
# print(res)
# #强转列表list()
# print(list(res))
# #转集合
# print(set(res))
# res=range(0,101)
# print(list(res))
# #求出0-100之间的所有偶数的和 和 所有奇数和
# for item in range(101):
#     sum=0#初始值 用来存储我们求的和
#     sum=sum+item
# print(sum)
#
# sum_1=0
# for item in range(1,101,2):
#     sum_1=sum_1+item
# print('奇数和:',sum_1)
# sum_2=0
# for item in range(0,101,2):
#     sum_2=sum_2+item
# print('偶数和:',sum_2)
#解法2：
# sum_1=0
# sum_2=0
# for item in range(101):
#     if item%2==0:#说明这个是偶数
#         sum_2=sum_2+item
#     else:
#         sum_1=sum_1+item
# print('奇数和:', sum_1)
# print('偶数和:',sum_2)
#嵌套循环：循环里面还有循环
# p=[[1,2,3],[4,5,6],[7,8,9]]
# for a in p:#外层循环
#     for item in a:#内层循环
#         print(item)
# *
# **
# ***
# ****
# *****
# p=[['*'],['*','*'],['*','*','*'],['*','*','*','*'],['*','*','*','*','*']]
# for i in range(1,6):#1 2 3 4 5 i=1 i=2
#     for j in range(1,i+1):#range(1,2) range(1,3)
#         print('*',end='') #end 防止换行
#     print()
#for循环：有限次数的循环
#while循环：可以无限次数的循环-死循环 同时 如果可以好好利用 用利用 有条件控制的口罩
#while循环语法
#while 条件表达式： #循环体
#条件表达式：跟if是一样的
#1.一般逻辑运算 比较运算 成员运算
#2.非0 个非空的数据表示true 为0和为空的数据 表示false
#3.可以直接用布尔值代替表达式
#运行模式：先判断while后面的条件 满足 就执行循环体 不满足的话 不执行
#执行完毕之后 再次判断while后面的条件 满足就执行循环体 不满足 不执行
#如此反复
#怎么达到  不对绝对的true 也不是绝对的false
#1：基本解决方法：break 终止循环 如果用的不好的话 就是执行一次
#2：进阶使用：break+条件 条件就是你规定他循环多少次
#3：高级使用：必要的时候 脱离break 自由自在
# continue 刹车点一下，继续下一次循环
# while True:
#     print('我是一个死循环')
#     break#break 终止循环
# a=0
# while True:
#     a+=1
#     print('a的值',a)
#     if a==10:
#         break
#     print('我是一个死循环')
#高级使用
# a=0
# while a<9:
#     a+=1
#     print('a的值',a)
#     print('我是一个死循环{0}'.format(a))

#一个足球队在寻找年龄在10岁到12岁的小女孩（包括10-12岁）加入
#编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄
#然后显示一条消息指出这个人是否可以加入球队，询问3次后，输出满足条件的总人数。
count=0#满足条件的人数
# for itme in 'abc':
#     age=int(input('同学，请问你今年多大了？请输入年龄：'))#int转了整数
#     if 10<=age<=12:
#         sex=input('方便填写一下的性别吗？请输入性别：')
#         if sex=='f':
#             print('恭喜你，满足条件，可以加入我们的女子球队')
#             count+=1#满足条件就加1
#         if sex=='m':
#             print('恭喜你，满足条件，可以加入我们的男子球队！')
#             count += 1  # 满足条件就加1
#     else:
#             print('很遗憾，你的年龄不符合条件，不能加入球队！')
# print('满足条件的总人数是:{0}'.format(count))
# print('满足条件的女性人数有：{0}个'.format(a))

a=0
while True:
    a+=1
    print('a的值',a)
    print('我是一个死循环{0}'.format(a))
    if a==10:
        break
    else:
        continue # continue 刹车点一下，继续下一次循环

