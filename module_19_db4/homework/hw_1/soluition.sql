SELECT a.teacher_id, avg(ag.grade) FROM assignments_grades AS ag
JOIN assignments AS a ON a.assisgnment_id = ag.assisgnment_id
GROUP BY a.teacher_id
ORDER BY ag.grade
LIMIT 1
