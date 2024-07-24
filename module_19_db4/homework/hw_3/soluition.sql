SELECT DISTINCT s.student_id from students_groups AS sg
LEFT JOIN students AS s ON sg.group_id = s.group_id
WHERE sg.teacher_id =
(SELECT a.teacher_id FROM assignments_grades AS ag
LEFT JOIN assignments AS a ON ag.assisgnment_id = a.assisgnment_id
GROUP BY a.teacher_id
ORDER BY avg(ag.grade) DESC
LIMIT 1)