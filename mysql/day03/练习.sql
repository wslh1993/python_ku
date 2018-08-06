-- 1． 查询Student表中的所有记录的sname、gender和class_id列。
select sname,gender,class_id from student;
-- 2、 查询教师所有的姓名即不重复的tname列。
select distinct tname from teacher;
-- 3、 查询Student表的所有记录。
select * from student;
-- 4、 查询Score表中成绩在60到80之间的所有记录。
select * from score where number between 60 and 80;
-- 5、 查询Score表中成绩为85，86或88的记录。
select * from score where number in (85,86,88);
-- 6、 查询Student表中性别为"女"的同学记录。
select * from student where sex = '女';
-- 7、 以age降序查询Student表的所有记录。
select * from student order by age desc;
-- 8、 以Cid升序、sid降序查询Score表的所有记录。
select * from score order by cid asc, sid desc;
-- 9、 查询"一年级一班"班的学生人数。
select count(s.id) from `student` as s inner join `class` as c
on s.class_id = c.id where c.name = '一年三班';
-- 10、查询Score表中的最高分的学生学号和课程号。
select student_id, course_id, student.name, course.name
from score inner join course on course.id=score.course_id
inner join student on score.student_id=student.id where 
`number`=(select max(number) from score);
-- 11、查询'3'号课程的平均分。
select avg(number) from score where course_id=3;
-- 12、查询Score表中至少有5名学生选修的课程id。
select count(student_id) as n, course_id from score group by course_id having n>=2;
-- 13、查询最低分大于70，最高分小于90的sid列。
select max(number) as m, min(number) as n, student_id from score group by student_id having m<90 and n>70;
-- 14、查询"一年级一班"所选课程的平均分。
select avg(number), course_id from score where student_id in (select student.id from student inner join class on student.class_id=class.id where class.name='一年八班') group by course_id;
-- 17、查询成绩高于学号为"5"最高分、课程号为"2"的成绩的所有记录。
SELECT * FROM score WHERE num>(SELECT MAX(num)FROM score WHERE sid=5) AND cid=2;
-- 18、查询和学号为6号同学相同年龄的所有学生的id、Sname和age列。
select * from student where age=(select age from student where id=6);
-- 19、查询"马杰"教师任课的学生成绩。
select number from score inner join course on 
score.course_id = course.id inner join teacher
on course.tid = teacher.id where teacher.name='马老师';
-- 20、查询选修某课程的同学人数多于5人的教师姓名。
select teacher.name from score inner join course on
score.course_id=course.id inner join teacher on
teacher.id=course.teacher_id group by course_id
having count(score.student_id)>=2;
-- 21、查询一年级二班和一年级一班全体学生的记录。
select * from student inner join class on student.class_id=class.id  
where  class.name in ('一年二班', '一年级一班');
-- 22、查询存在有85分以上成绩的课程.
SELECT cname FROM course WHERE id in (SELECT cid FROM score WHERE num>85);
-- 23、查询出"数学"教师所教课程的成绩表。
SELECT * FROM score INNER JOIN course ON score.cid=course.id WHERE course.cname='数学';
-- 24、查询所有教师和同学的所有信息.
SELECT * from teacher;
SELECT * from student;
-- 25、查询所有"女"教师和"女"同学的name、gender.
SELECT tname,sex from teacher where sex='女';
SELECT name,sex from student where sex='女';
-- 26、查询学生平均成绩比总平均成绩低的同学的学生名。 不会
select studet.name from student where student.id in (select student.id from student inner join score on score.sid=student.id where())group by sid;
-- 27、查询所有任课教师的Tname.
select tname from teacher where teacher.id in (select tid from course);
-- 28  查询所有未讲课的教师的Tname. 
select tname from teacher where teacher.id not in (select tid from course);
-- 29、查询至少有2名男生的班号。 不会
select class_id from student where (select count(id) from student group by class_id having sex='男');
-- 30、查询Student表中不姓"王"的同学记录。
select * from student where name not like '王%';
-- 31、查询Student表中最大和最小的年龄。
select max(age),min(age) from sudent;
-- 32、以班号和年龄从大到小的顺序查询Student表中的全部记录。
select * from student order by age asc,class_id desc;
-- 34、查询最高分同学的Sno、Cno和成绩列。
-- 35、查询和"李军"同性别的所有同学的Sname.
select name from student where sex=(select sex from student where sname='李军');
-- 36、查询和"李军"同性别并同班的同学Sname.
select name from student where sex=(select sex from student where sname='李军') and cid=(select name from student where sname='李军');
-- 37、查询所有选修"语文"课程的"男"同学的成绩表
select num from score inner join course on score.cid=course.id inner join student on student.id=score.sid where course.cname='语文' and student.sex='男';