-- 连接数据库
-- mysql -h 主机地址 -u 用户名 -p 密码
-- 例如:mysql -h 127.0.0.1 -uroot -proot
-- 创建数据库(注意指定默认编码, 可以避免后面由于编码不对导致的错误)
-- create database if not exists 数据库名 default charset=utf8;
-- 查看数据库
-- show database;
-- 删除数据库
-- drop database if exists 数据库名;
-- 使用数据库
-- use 数据库名;

-- 数据表字段(列)类型
-- 字符串: 
-- char 固定长度字符串
-- varchar 可变长度字符串
-- text 长文本字符串
-- 数字:
-- tinyint 微小整数
-- smallint 小整数
-- int 标准整数
-- bigint 超大整数
-- float 单精度浮点数
-- double 双精度浮点数
-- decimal 字符串形式的小数, 高精度要求的小数,例如:价格
-- 日期时间
-- date 日期
-- datetime 日期和时间
-- time 时间
-- timestamp 时间戳
-- year 年份

-- 创建数据表(列名和类型是必须的,后面的属性是可选的)
create table if not exists student(
  id int(11) not null auto_increment primary key comment '编号',
  name varchar(5) not null,
  age tinyint(3),
  sex char(2) default '男'
)engine=innodb charset=utf8 comment='学生表';
-- 字段的属性:
-- unsigned 无符号, 即没有负数, 只能给数字类型使用
-- zerofill 填充0, 不足的位数用0来填充
-- auto_increment 自动递增, 通常给主键列使用
-- null 允许为空值
-- not null 不允许为空
-- default 值   设置默认值
-- unique 唯一,不允许重复
-- comment '备注内容'  给字段或者表格本身添加说明文字

-- 查看当前数据库有哪些表 show tables；
-- 查看某张表的结构信息 desc 表名；
-- 删除表 drop table 表名；

-- 修改表名 alter table 表名 rename as 新表名；
-- 添加字段 alter table 表名 add 字段名 类型 [其它属性选项]
-- 修改字段 alter table 表名 modify 字段名 类型 [其它属性选项]
-- 修改字段名 alter table 表名 change 旧字段名 新字段名 类型 [其它属性选项]
-- 删除字段 alter table 表名 drop 字段名


-- 添加数据
-- insert into 表名(字段名列表...) values (值列表..)
-- 字段名列表与值列表必须一一对应
-- 如果不指定字段名列表，则表示给所有字段都要添加值（不建议这么做）
-- 例如：
insert into class (name) values ('一年一班');

-- 更新数据
-- update 表名 set 列名=更新值, ... where 条件语句
-- 更新哪些列，就写哪些列即可，多个列之间逗号隔开，没有数量限制
-- where 条件语句是可选择的，如果不指定则表示更新所有数据
-- where 条件语句的基本写法：
-- where 列名=值 
-- where 列名>值
-- where 列名<值
-- where 列名<>值    不相等
-- where 列名!=值    不相等
-- where 列名>=值    大于或等于
-- where 列名<=值    小于或等于
-- where 条件1 or 条件2  或者
-- where 条件1 and 条件2 并且
-- where 列名 not null  非，字段不为空
-- where 列名 between m and n     列的值在m与n之间（包括m和n）
-- 例如：
-- where age between 1 and 10  年龄在1到10时间均可
-- 等同于
-- where age >= 1 and age <= 10
-- where 列名 in (a, b, c, d ...)  列到值与括号中的任意一个值相等即可
-- 例如：
-- where name in ('一年一班', '一年五班', '二年三班') 名称等于三个班级中任意一个均可
-- 等同于
-- where name='一年一班' or name='一年五班' or name='二年三班'

-- 例如：
update class set name = 'Hello';  修改所有班级名称为Hello

-- 删除数据
-- delete from 表名 where 条件
-- 清空表的数据
-- truncate table 表名；
-- 不同：
-- delete语句删除数据可以指定条件，删除某些数据，truncate就是清空所有数据
-- delete删除数据不会重置自增列的值，而truncate会重置自增列的值

-- 查询数据
-- select * from 表名; 查看表里面的所有数据
-- select 字段名列表... from 表名 where 条件
-- 多个字段之间用逗号隔开
-- * 表示所有字段（实际应用中应该避免使用*）
-- as 子句，给字段或表格起别名
-- distinct 去除查询结果中重复的值

-- 模糊查询：% 用于匹配任意个任意字符    _ 用于匹配一个任意字符
-- 字段名  like  值;
-- 查询姓张的学生
-- select name, age, sex from student name like '张%';

-- 对查询结果排序：order by 字段名 asc/desc;
-- asc 是默认值，表示升序
-- desc 表示降序
-- 排序可以用多列进行排序， 多列表列名之间用逗号隔开，方式是先用第一个列排序，如果结果中有重复的值，才用第二个列排，如果还有重复，继续使用第三个列排。。。，如果结果中没有重复的值，则后面的排序就不执行了。
-- 每个字段都可以指定自己的排序方式
-- select * from student order by class_id asc, age desc;
-- 注意：order by 语句必须写在where语句的后面，不能写在where的前面

-- 限制查询结果的行数
-- limit m, n
-- m 为一个整数，表示起始行的索引，从0开始，可省略，省略则默认为0
-- n 为一个整数，表示查询几行

-- 外键约束
-- 当一个表的某个字段是引用另外一个表的某个字段的时候，就可以建立一个外键约束，目的在于强制验证表格中引用的数据是真是存在的。
-- 通常的做法是将表格中的某个字段的值指定为被引用的表格的主键。
-- 建立外键的两张表格就有了强制约束的关系，把被引用的表叫做“主表（父表）”，另外一个表叫做“从表（子表）”
-- 建立外键约束需要在子表中指定
-- 例如：
create table student2( 
  id int(11) primary key auto_increment, 
  name varchar(6) not null, 
  class_id int(11),
  constraint student_class_id foreign key (class_id) references class(id))engine=myisam;
