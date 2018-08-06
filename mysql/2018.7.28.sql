-- 链接库mysql -uroot -proot
-- 建库liuhe 指定默认编码为utf8
create database liuhe default charset=utf8;
-- 查看有哪些库
show databases; 
-- 操作liuhe
use liuhe;
-- 建student表
create table if not exists student(
  id int(11) not null auto_increment primary key comment '编号',
  name varchar(5) not null,
  age tinyint(3),
  sex char(2) default '男'
)engine=innodb charset=utf8 comment='学生表';
-- 建teacher表
 create table if not exists teacher(
  id int(11) not null auto_increment primary key comment '编号',
  name varchar(5) not null,
  year tinyint(3),
  sex char(2)
)engine=innodb charset=utf8 comment='教师表';
-- 建class表
 create table if not exists class(
  id int(11) not null auto_increment primary key comment '编号',
  class_name varchar(8) not null
)engine=innodb charset=utf8 comment='班级表';
-- 建course表
create table if not exists course(
  id int(11) not null auto_increment primary key comment '编号',
  cname varchar(8) not null,
  tid int(11)
)engine=innodb charset=utf8 comment='课程表';
-- 建score表
create table if not exists score(
  id int(11) not null auto_increment primary key comment '编号',
  sid int(11),
  cid int(11),
  num float(5)
)engine=innodb charset=utf8 comment='成绩表';
-- 查看liuhe下的表
show tables;