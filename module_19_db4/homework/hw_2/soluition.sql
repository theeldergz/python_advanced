SELECT st.full_name, avg(ag.grade) FROM assignments_grades ag
JOIN students AS st ON ag.student_id = st.student_id
GROUP BY ag.student_id
ORDER BY avg(ag.grade) DESC
LIMIT 10