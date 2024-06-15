SELECT Product.maker, Laptop.speed FROM Product
JOIN Laptop ON Product.model = Laptop.model
WHERE Product.type LIKE 'Laptop' AND Laptop.hd >= 10

