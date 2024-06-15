SELECT name FROM ships WHERE class = name
UNION
SELECT ship AS name FROM  Classes AS cls, Outcomes AS ou WHERE cls.class = ou.ship
