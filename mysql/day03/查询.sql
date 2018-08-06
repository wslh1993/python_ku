-- 连接查询
-- 内连接：查两张表共有的数据，即两张表都能匹配到的数据才会被查出来。
-- select 字段列表... from 表1 inner join 表2 on 两表关系 where 条件
-- 左连接：总是查左表的所有数据，右表与左表匹配的，没有匹配的则显示为NULL
-- select 字段列表... from 表1 left join 表2 on 两表关系 where 条件
-- 右连接：总是查右表的所有数据，左表与右表匹配的，没有匹配的则显示为NULL
-- select 字段列表... from 表1 right join 表2 on 两表关系 where 条件

-- 把一个查询语句的结果作为另外一个语句的条件叫做子查询
-- 查询和张5学同样课程的学员的成绩
select course.id from course inner join score on 
course.id = score.course_id inner join student
on score.student_id = student.id where
student.`name` = '张5'
-- 查询和张5学同样课程的学员的成绩
select * from score where course_id=(select course.id from course inner join score on course.id = score.course_id inner join student
on score.student_id = student.id where
student.`name` = '张5')

-- 年龄大于15岁的学生的成绩
select * from score where student_id in 
(select id from student where age>15)


-- count(字段名) 求总行数
-- sum(字段名) 求和
-- agv(字段名) 平均数
-- max(字段名) 最大值
-- min(最小值) 最小值


-- 一共有多少个学员
select count(id) from student;

-- 平均成绩
select avg(number) from score;

-- 总成绩
select sum(number) from score;

-- 最高分
select max(number) from score;

-- 最低分
select min(number) from score;

-- 分组查询，将查询结果按照某个字段进行分组。
-- 要分组，必须有统计（聚合）函数
-- 对分组中的聚合函数过滤，必须使用having关键字，不能使用where
-- 其它普通的条件依然使用where
select avg(number) as n from score group by student_id having n > 60;
-- 分组子句必须在where语句后面
select avg(number) as n from score where student_id > 4
group by student_id having n > 60;

-- 查询的完整语法：
SELECT   [ALL | DISTINCT] 
{  * |  table.* | [ table.field1 [ as  alias1] [,table.field2 [as  alias2]][,…]] }
FROM  table_name  [ as  table_ alias  ]
    [left|out|inner  join  table_name2]    #联合查询
	[ WHERE  … ]   	#指定结果需满足的条件
	[ GROUP BY …]	#指定结果按照哪几个字段来分组
	[ HAVING …]	#过滤分组的记录必须满足的次要条件
	[ ORDER BY… ]	#指定查询记录按一个或者多个条件排序
	[ LIMIT  {   [ offset,] row_count | row_count OFFSET offset   }] ;  #指定查询的记录从哪条至哪条


