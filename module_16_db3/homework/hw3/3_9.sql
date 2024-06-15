SELECT DISTINCT pr.maker FROM Product as pr
JOIN PC as pc ON pr.model = pc.model
WHERE pc.speed >= 450
