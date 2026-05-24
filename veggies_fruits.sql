-- 1. Відображення всієї інформації з таблиці

SELECT * FROM items;

-- 2. Відображення усіх овочів

SELECT * FROM items WHERE type = 'овоч';

-- 3. Відображення усіх фруктів

SELECT * FROM items WHERE type = 'фрукт';

-- 4. Відображення усіх назв овочів та фруктів

SELECT name FROM items;

-- 5. Відображення усіх унікальних кольорів

SELECT DISTINCT color FROM items;

-- 6. Відображення фруктів певного кольору

SELECT * FROM items WHERE type = 'фрукт' AND color = 'жовтий';

-- 7. Відображення овочів певного кольору

SELECT * FROM items WHERE type = 'овоч' AND color = 'червоний';
