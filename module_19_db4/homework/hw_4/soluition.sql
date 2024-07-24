SELECT
    group_num,
    ROUND(AVG(overdue), 0),
    MAX(overdue),
    MIN(overdue)
FROM (
SELECT _as.group_id AS group_num, COUNT(_as.assisgnment_id) AS overdue FROM assignments AS _as
LEFT JOIN assignments_grades AS sg ON sg.assisgnment_id = _as.assisgnment_id
WHERE sg.date > _as.due_date
GROUP BY group_num
)