/* 2、 查询“语文”课程比“数学”课程成绩高的所有学生的学号； */
select * from score inner join student on
student.id = socre.student_id where 
(select number from score inner join course on
course.id=score.course_id where course.name='HTML') >
(select number from score inner join course on
course.id=score.course_id where course.name='JS')
3、 查询平均成绩大于60分的同学的学号和平均成绩；?
4、 查询所有同学的学号、姓名、选课数、总成绩；
select student.id, student.name, count(score.id),
sum(score.number) from student inner join score
on student.id=score.student_id group by student.id
5、 查询姓“郭”的老师的个数；
6、 查询没学过“郭靖”老师课的同学的学号、姓名；
select * from student where id in (select student_id from score where course_id not in (select id from course inner join teacher on course.teacher_id=teacher.id where teache.name='郭靖'))
7、 查询学过“001”并且也学过编号“002”课程的同学的学号、姓名；
8、 查询学过“郭靖”老师所教的所有课的同学的学号、姓名；
9、 查询课程编号“002”的成绩比课程编号“001”课程低的所有同学的学号、姓名；
10、查询有课程成绩小于60分的同学的学号、姓名；
select * from student where id in (select student_id from score where number < 60)
11、查询没有学全所有课的同学的学号、姓名；
12、查询至少有一门课与学号为“001”的同学所学相同的同学的学号和姓名；
select * from student wehre id in (select student_id from score where course_id in (select course_id from score where student_id=1) and student_id!=1)
13、查询至少学过学号为“001”同学所有一门课的其他同学学号和姓名；
14、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；
17、按平均成绩从低到高显示所有学生的“生物”、“数学”、“物理”三门的课程成绩，按如下形式显示： 学生ID,生物,数学,物理,课程数,平均分；
18、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
19、按各科平均成绩从低到高和及格率的百分数从高到低顺序；
select avg(number) as a from score group by course_id order by a, (select count(id) from score where number>60)/(select count(id) from score) desc;
20、课程平均分从高到低显示（现实任课老师）；
21、查询各科成绩前三名的记录:(不考虑成绩并列情况)?
22、查询每门课程被选修的学生数；
select count(student_id) from score group by course_id
23、查询出只选修了一门课程的全部学生的学号和姓名；
select count(course_id) as a from score group by course_id having a=1
24、查询男生、女生的人数；
25、查询姓“蔡”的学生名单；
26、查询同名同姓学生名单，并统计同名人数；
27、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
select avg(number) as a from score group by course_id order by a, course_id desc
28、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；
select avg(nubmer), student_id as a from score inner join student on student.id = score.student_id group by student_id having a > 85
29、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
select * from score inner join course on score.course_id = course.id wehre score.number<60 and course.name='数学'
30、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名；?
select * from score inner join student on student.id=score.student_id where score.number>80 and score.course_id=3
31、求选了课程的学生人数
select count(student_id) from score
33、查询各个课程及相应的选修人数；
select count(student_id) from score group by course_id
34、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
select student_id,course_id,number from score as a where number in (select number from score where id!=a.id and a.course_id!=course_id)
35、查询每门课程成绩最好的前两名；
select * from score where course_id=1 order by number desc limit 2
36、检索至少选修两门课程的学生学号；
select count(course_id) as a from score group by student_id having a >= 2
37、查询全部学生都选修的课程的课程号和课程名；
select count(student_id) as a from score group by course_id having a = (select count(id) from student)
39、查询两门以上不及格课程的同学的学号及其平均成绩；
select avg(number), student_id from score where student_id in (select student_id from score where number<70 group by student_id having count(course_id)>=2) group by student_id
