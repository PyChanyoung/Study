/* 
primary key: 
조인을 하면 컬럼의 갯수가 늘어나고, 유니언을 하면 세로로 길어진다.
유니언을 하려면 동일한 컬럼이어야 한다.
Exmaple of Union>
SELECT * FROM GRADE_FIRST
UNION
SELECT * FROM GRADE_SECND
UNION
SELECT * FROM GRADE_THIRD

Example Syntax of JOIN>
<inner join>
select distinct a.class_id, 
from
(class a
join student b
ON a.student_id = b.student_id)
where b.name = '[DATA]'

<left join>
select distinct a.class_id, 
from
(class a
left join student b
on a.student_id = b.student_id)
where b.student_id = '[DATA]'

aggregate function
.
.
max()
min()
count()
sum()

*/