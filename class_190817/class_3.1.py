# -*- coding: utf-8 -*-
# @Time     :2020/3/4 上午 10:47
# @Author   :yutq.test
# @Email    :646642124@qq.com

# a=input('请输入一个数据：')
# print(a)

# a=10
# b=100
# print(type(10.1))
# type 查看数据类型
a='hello python13'
print(len(a))
#len 统计长度
#索引
print(a[6]) #6为'hello python13'p的索引 正序从0开始
print(a[-8]) #-8为倒序
print(a[0])
#3.切片：用法-变量名[m:n:k]
# m你要从哪里开始切  n你切到哪个位置结束 k隔几个切一刀
#m开始取值的索引位置  n取值结束的位置 k取值隔开的距离（步长，隔开几个字符）
# 取左不取右 取n-1
# m为左n为右
print(a[0:14:1])

#字符串拼接 +
s_1='hello'
s_2='卡哇伊'
a=20 #转成字符串 str（） 强制转换
print(s_1+s_2+str(a)) #方法1 str（）
print(s_1+s_2,a) #方法2 使用 , 相隔
# ，是隔开的用法
print(1,2,3,4) #演示

#格式化输出方法1
age=18 #整数
height=170.36  #浮点数
hobby='打篮球' #字符串
print('''---小明个人档案---
      年龄：%s
      身高：%0.1f 
      业余爱好：%s'''%(age,height,hobby))
# %d代表整数 %f代表浮点数 %s代表字符  %s可以代表所有数据类型
#身高：%0.1f 0.1f可以四舍五入
# %2s 表示取浮点数后2位
#格式化输出方法2
print('''---Bay max个人档案---
    年龄：{0}
    身高：{1}
    业余爱好：{2}'''.format(age,height,hobby))
# .format格式化输出

# 切换大小写 upper()字符串变大写  lower()符串变小写 swapcase大小写互换
b='hello pythin13y'
c='HELLo pYthin13y'
print(b.upper())
print(c.swapcase())
# replace 替换
print(b.replace('e','测试')) # 打印结果 h测试llo pythin13y
#find 查找元素 没有找到就返回-1
print(b.find('y'))
# count 表示数值重新次数
d='测试试试，H'
print(d.count('试'))
print(d.isdigit()) #方法检测字符串是否只由数字组成。False
print(d[1].islower())#方法检测字符串是否由小写字母组成。True
print(d.isupper())# 方法检测字符串中所有的字母是否都为大写。True
print('@铁'.join(d))# 隔1字符加一个需要插入的字符串


