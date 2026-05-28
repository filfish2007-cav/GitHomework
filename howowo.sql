-- 1

SELECT * FROM items
WHERE type ILIKE 'овоч'
  AND calories < 30;


-- 2

SELECT * FROM items
WHERE type ILIKE 'фрукт'
  AND calories BETWEEN 40 AND 60;

-- 3

SELECT * FROM items
WHERE type ILIKE 'овоч'
  AND name ILIKE '%Томат%';

-- 4

SELECT * FROM items
WHERE description ILIKE '%калі%';

-- 5

SELECT * FROM items
WHERE color ILIKE 'жовтий'
   OR color ILIKE 'червоний';

-- 6

SELECT COUNT(*) AS total_vegetables
FROM items
WHERE type ILIKE 'овоч';

-- 7

SELECT COUNT(*) AS total_fruits
FROM items
WHERE type ILIKE 'фрукт';

-- 8

SELECT COUNT(*) AS total_count
FROM items
WHERE color ILIKE 'зелений';

-- 9

SELECT color, COUNT(*) AS item_count
FROM items
GROUP BY color
ORDER BY item_count DESC;

-- 10

SELECT color
FROM items
GROUP BY color
ORDER BY COUNT(*) ASC
LIMIT 1;

-- 11

SELECT color
FROM items
GROUP BY color
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 12

SELECT MIN(calories) AS min_calories
FROM items;

-- 13

SELECT MAX(calories) AS max_calories
FROM items;

-- 14

SELECT ROUND(AVG(calories), 2) AS average_calories
FROM items;

-- 15

SELECT name, calories
FROM items
WHERE type ILIKE 'фрукт'
ORDER BY calories ASC
LIMIT 1;

-- 16

SELECT name, calories
FROM items
WHERE type ILIKE 'фрукт'
ORDER BY calories DESC
LIMIT 1;
