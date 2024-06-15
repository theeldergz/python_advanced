SELECT DISTINCT tmp.model, tmp.price FROM Product AS pr
JOIN (SELECT model, price  FROM PC
UNION ALL
SELECT model, price  FROM Laptop) AS tmp ON pr.model = tmp.model
WHERE pr.maker = 'B'
