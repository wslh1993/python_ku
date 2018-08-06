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
 create table if not exists teacher(
  id int(11) not null auto_increment primary key comment '编号',
  name varchar(5) not null,
  year tinyint(3),
  sex char(2)
)engine=innodb charset=utf8 comment='教师表';
 create table if not exists class(
  id int(11) not null auto_increment primary key comment '编号',
  class_name varchar(8) not null
)engine=innodb charset=utf8 comment='班级表';
create table if not exists course(
  id int(11) not null auto_increment primary key comment '编号',
  cname varchar(8) not null,
  tid int(11)
)engine=innodb charset=utf8 comment='课程表';
create table if not exists score(
  id int(11) not null auto_increment primary key comment '编号',
  sid int(11),
  cid int(11),
  num float(5)
)engine=innodb charset=utf8 comment='成绩表';
-- 字段的属性:
-- unsigned 无符号, 即没有负数, 只能给数字类型使用
-- zerofill 填充0, 不足的位数用0来填充
-- auto_increment 自动递增, 通常给主键列使用
-- null 允许为空值
-- not null 不允许为空
-- default 值   设置默认值
-- unique 唯一,不允许重复
-- comment '备注内容'  给字段或者表格本身添加说明文字
