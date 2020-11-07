# -*- coding: utf-8 -*-
# @Time     :2020/6/16 下午 9:38
# @Author   :yutq.test
# @Email    :646642124@qq.com
# @File     :class_8_if.py
#if 语句
#代码从上往下执行
#条件语法 if...else
#语法：
# 条件表达式 一般逻辑运算符 比较运算符 成员运算符
#if 条件表达式 ：
    #代码
#else：
    #代码

# gift='鲜花'
# if gift=='巧克力':
#     print('表白成功')
# elif gift=='鲜花1':
#     print('表白成功啦！')
# else:
#     print('表白失败')
    #if elif 必须加条件表达式 else不能加任何条件
    #1.非 0和非空的数据表示 true 为0和为空的数据 表示false (非常重要)
 #1.1例子： a={'name':1}
# gift = '鲜花'
# a={'name':1}
# if a :
#     print('表白成功')
# elif gift == '鲜花1':
#     print('表白成功啦！')
# else:
#     print('表白失败')
 #只要返回值是true 或者是false 都可以作为if 或者elif 后面的条件表达式
#练习：从控制台获取一个数据 根据成绩判断
# #如果>80优秀 >70良好 >=60及格 <60不及格 数据范围是0-100
#查看数据类型
# test=input('请输入一个数据:')
# print(type(test))
test=int(input('请输入你的成绩:'))#利用input从控制台获取的数据都是数据都是字符串练习
print(test)
if test>100 or test<0:
    print('数据范围只能在0-100之间')
elif test>80:
    print('优秀')
elif test>70:
    print('良好')
elif test>=60:
    print('及格')
elif test<60:
    print('不及格')
else:
    print('不及格')
