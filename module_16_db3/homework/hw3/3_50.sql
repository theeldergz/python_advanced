SELECT DISTINCT battle FROM Ships AS sh
INNER JOIN Outcomes AS ou ON sh.name = ou.ship
WHERE class = 'Kongo'
