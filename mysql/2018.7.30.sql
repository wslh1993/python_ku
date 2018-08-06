-- 链接库mysql -uroot -proot
-- 操作liuhe
use liuhe;
-- 给student,teacher,score,class,course加数据
insert into student(name,age,sex,class_id) values('小马',16,'女',2);
insert into teacher(tname,sex) values('小刚','男'),('小彭','男'),('小李','男'),('老马','男');
insert into score(sid,cid,num) values(1,1,60),(1,2,70),(1,3,80),(2,1,90),(2,2,77);
insert into class(class_name) values('AI8'),('AI9'),('AI10'),('AI11'),('AI12');
insert into course(cname,tid) values('数学',3),('语文',2),('英语',1);
-- 1`查询student表中所有name sex class_id
select(name),(sex),(class_id) from student;
-- 2`查询所有不重复的教师名字
select distinct tname from teacher;
-- 3`查询所有student的记录
select * from student;
-- 4`查询Score表中成绩在60到80之间的所有记录
select * from score where num between 60 and 80;
-- 5`查询Score表中成绩为85，86或88的记录
select * from score where num in(85,86,88);
-- 6`查询Student表中性别为“女”的同学记录
select * from student where sex='女';
-- 7`以age降序查询Student表的所有记录
 select * from student order by age desc;
-- 以Cid升序、sid降序查询Score表的所有记录
select * from score order by cid asc,sid desc;
select count(id) from student where class_id in (select class.id from class where class_name='ai8');
select sid,cid from score where num=(select max(num) from score);
select name from student where id=(select sid from score where num=(select max(num) from score));
select cname from course where id=(select cid from score where num=(select max(num) from score));
select name,cname from student,course where student.id=(select sid from score where num=(select max(num) from score)) and course.id=(select cid from score where num=(select max(num) from score));
select avg(num) from score where cid=3;