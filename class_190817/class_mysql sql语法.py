# -*- coding: utf-8 -*-
# @Time     :2020/10/25 下午 3:51
# @Author   :yutq.test
# @Email    :646642124@qq.com
# @File     :class_mysql sql语法.py
#  查询篇
# 别名 as 可以省略
# distinct 过滤重复记录
# where条件
# 比较运算符 = < <= > >=  !=或者<>
# 逻辑运算符 and 2个都成立 or 2选1 not 求非
# 模糊查找 like % _
# select * from a where age like ‘%3’
# 范围查找 in 非连续查找  连续查找： between start（开始值） and stop（结束值） between适用 数字 英文字母
# 空值判断 is null  判断非空 is not null
# 排序 order by  asc从小到大 dec从大到小
# 聚合函数 count返回指定组中项目的数量。  max返回指定数据的最大值。 min返回指定数据的最小值。 sum返回指定数据的和，只能用于数字列，空值被忽略。 avg返回指定组中的平均值，空值被忽略。
# 数据分组 group by  having 先分组聚合统计，在统计结果中筛选
# 显示指定数量的记录 limit有限指定 star count
# 左连接 查询2表中满足条件的相同部分 加上左表特有的数据 左表不存在的数据使用null填充
# select * from 表1名 left join 表2名 on 表1.字段 = 表2.字段
# 内连接  只查询2表中满足条件的部分
# 语法 select * from 表1 inner join 表2  on 表1.字段 = 表2.字段
# select * from 表1 inner join 表2  on 表1.字段 = 表2.字段 inner join 表 3  on 表4.字段 = 表5.字段 where = '8888'
# select * from 表1 inner join 表2  on 表1.字段 = 表2.字段 order by 表1.字段 desc limit1
# 隐藏式语法 select * from 表1 ，表2 where 表1.字段 = 表2.字段
# 别名的使用 select * from 表1 no1 inner join 表2 no2  on no1.表1.字段 = no2.表2.字段
# 右连接 查询的结果为2个表特有的数据，对于右表中不存在的数据使用null填充
# select * from 表1名 right join 表2名 on 表1.字段 = 表2.字段
#   x写sql三步法
# 1.搭框架
#     基本的select语句框架搭建起来，把相应的多表也联合起来
# 2.看条件
#     决定where后面的具体条件
# 3.显示的字段
#     select 后面到底要显示什么字段
# 多表联合查询，同名字段处理 需要表名.字段名 加以区分
# select 表名.字段名 from 表1 inner join 表2  on 表1.字段 = 表2.字段
#
#


