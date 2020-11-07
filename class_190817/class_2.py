# -*- coding: utf-8 -*-
# @Time     :2019/8/25 上午 9:02
# @Author   :yutq.test
# @Email    :646642124@qq.com
# @File     :class_2.py

#字符串 str 主要处理文本数据
# 打印原生字符串 加r a = r"I\'M itcastYY"
# 成对的双引号可以嵌套成对的单引号  "123‘445’678"
# 成对的单引号可以嵌套成对的双引号  ' " " '
# 字符串定义细节
# 单引号字符串
# 双引号字符串
# 三引号字符串
# 特殊符号处理

a='hello python13'
#hello python13  14个字符串包含空格
#常规用法：字符串的取值和切片
#1.字符串里面的元素：单个字符算一个元素（数字 字母 符号 中文）
#2.统计字符串的长度：len（a）
print(len(a))
#编号是从0开始的 取值方式：变量名 [索引]
#  h e l l o   p y t h o  n  1  3
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13  正序
print(a[6])
#  h  e    l   l   o      p  y  t  h  o  n  1  3
#-14 -13  -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1  反序
print(a[-1])
print(a[0])
#3.切片：用法-变量名[m:n:k]
# m你要从哪里开始切  n你切到哪个位置结束 k隔几个切一刀
#m开始取值的索引位置  n取值结束的位置 k取值隔开的距离（步长）取左不取右 取n-1
print(a[0:13:1]) #取值+1
print(a[0:13:3]) # 0 3 6 9 12
#把a字符串里面编号为偶数的元素用切片 打印出来
print(a[::2])
 # h l o p t o 1 偶数位
 # 把a字符串利用切片实现倒序输出
print(a[14::-1]) #方法1
print(a[::-1]) #方法2
#字符串拼接 +
s_1='hello'
s_2='卡哇伊'
a=20 #转成字符串 str（） 强制转换
print(s_1+s_2+str(a)) #方法1 str（）
print(s_1+s_2,a) #方法2 使用 ,
# , 使用演示
print(1,2,3,4)
#格式化输出方法1
age=18 #整数
height=170.34  #浮点数
hobby='打篮球' #字符串
# %s匹配所有数据类型
# % 占位符 可以达到换行效果
print('''-----档案-----
      年龄是：%s
      身高是：%0.2s
      业余爱好是：%s'''%(age,height,hobby))# %格式化输出 连接变量名
#格式化输出方法2: {} 编号
print('''---Bay max个人档案---
年龄：{0}
身高：{1}
业余爱好：{2}'''.format(age,height,hobby)) # 0开始编号坑 按顺序编号
# .format 格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
# format  基本语法是通过 {} 和 : 来代替以前的 % 。

#函数
a='hello pythin13y'
b='HELLo pYthin13y'
# 切换大小写 upper()字符串变大写  lower()符串变小写 swapcase大小写互换
print(a.upper())
print(a.lower())
print(b.swapcase())
# replace 替换
s=a.replace('n','N')
s=a.replace('l','@',1) #当有2个一样的字符串时默认全部替换，数字加1表示替换1个
print(s)
#find 查找元素 没有找到就返回-1
print(a.find('hello'))
#单个字符串如果找到了 返回的是遇到的第一个元素的索引的值
print(a.find('13y'))
#子字符串 长度大1 如果找到了 就返回子字符串所在字符串里面的第一个
#capitalize() 首字符大写
print(a.capitalize())
# 布尔值判断  False True
b='11'
d='ssr'
print(b.isdigit()) #方法检测字符串是否只由数字组成。False
print(d.islower())#方法检测字符串是否由小写字母组成。True
print(d[1].islower())
c='ABC'
print(c.isupper())# 方法检测字符串中所有的字母是否都为大写。True
#  join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
print('@'.join(a)) #h@e@l@l@o@ @p@y@t@h@i@n@1@3@y
a='hello pythin13y'
print(a.split(' '))#切割 返回的是列表 #  打印结果：['hello', 'pythin13y']
