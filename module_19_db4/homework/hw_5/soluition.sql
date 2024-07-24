SELECT group_id, COUNT(student_id) AS student_count FROM students
GROUP BY group_id

SELECT s.group_id, AVG(ag.grade) as avg_grade FROM assignments_grades AS ag
JOIN students as s ON ag.student_id = s.group_id
GROUP BY s.group_id

SELECT DISTINCT COUNT(*) AS not_due FROM students AS st
LEFT JOIN assignments_grades AS ag ON st.student_id = ag.student_id
WHERE ag.grade is NULL

SELECT DISTINCT COUNT(*) AS late_due FROM assignments_grades AS ag
LEFT JOIN assignments AS a ON a.assisgnment_id = ag.assisgnment_id
WHERE ag."date" < a.due_date

SELECT st.group_id, COUNT(*) AS repeat_test_count FROM students AS st
LEFT JOIN assignments_grades AS ag ON ag.student_id = st.student_id
WHERE st.student_id IN (SELECT ag.student_id FROM assignments_grades AS ag
GROUP BY ag.student_id
HAVING COUNT(ag.grade) > 1)
GROUP by st.group_id

