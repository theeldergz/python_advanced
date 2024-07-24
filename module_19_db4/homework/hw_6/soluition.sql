SELECT AVG(ag.grade) FROM assignments_grades AS ag
WHERE ag.assisgnment_id IN (SELECT assisgnment_id FROM assignments
WHERE assignment_text LIKE "%выучить%" OR
assignment_text LIKE "%прочитать%")
