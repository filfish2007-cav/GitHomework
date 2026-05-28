-- Для бази даних «Таблиця» створіть такі запити:
-- 1. Вивести вміст таблиці палат.
-- SELECT * FROM WARDS
-- 2. 3. Вивести прізвища та телефони усіх лікарів.
-- SELECT surname, phone FROM doctors
-- Вивести усі поверхи без повторень, де розміщуються
-- палати.
-- SELECT DISTINCT floor FROM wards
-- 4. Вивести назви захворювань під назвою « Name of
-- Disease» та ступінь їхньої тяжкості під назвою «Severity
-- of Disease».
-- SELECT name AS name_of_disease, severity AS "severity of Disease"
-- FROM diseases
-- 5. Вивести назви відділень, які знаходяться у корпусі 5
-- з фондом фінансування меншим, ніж 30000.
-- SELECT name FROM departments
-- WHERE building = 3 AND financing < 4000000
-- 6. Вивести назви відділень, які знаходяться у корпусі 3 з
-- фондом фінансування у діапазоні від 12000 до 15000.
-- SELECT name FROM departments
-- WHERE building = 2 AND financing < 4000000 AND financing > 2000000
-- 8. Вивести назви палат, які знаходяться у корпусах 4 та
-- 5 на 1-му поверсі.
-- SELECT name,building,floor FROM wards
-- WHERE building IN(2,3) AND floor = 1
-- WHERE (building = 2 OR building = 3) AND floor = 1
-- 9. Вивести назви, корпуси та фонди фінансування від-
-- ділень, які знаходяться у корпусах 3 або 6 та мають
-- фонд фінансування менший, ніж 11000 або більший
-- за 25000.
SELECT name, building, financing
FROM departments
WHERE (building = 3 OR building = 6)
  AND (financing < 1000000 OR financing > 3000000);
-- 10. Вивести прізвища лікарів, зарплата (сума ставки та
-- надбавки 120) яких перевищує 1500.
SELECT surname
FROM doctors
WHERE (salary + 120) > 1500;
-- 11. Вивести прізвища лікарів, у яких половина зарплати
-- перевищує триразову надбавку у вигляді 500.
SELECT surname
FROM doctors
WHERE (salary / 2.0) > (3 * 500);
-- 12. Вивести назви обстежень без повторень, які прово-
-- дяться у перші три дні тижня з 12:00 до 15:00.
SELECT DISTINCT name
FROM examinations
WHERE day_of_week IN (1, 2, 3)
  AND start_time >= '12:00:00'
  AND end_time <= '15:00:00';
-- 13. Вивести назви та номери корпусів відділень, які зна-
-- ходяться у корпусах 1, 3, 8 або 10.
SELECT name, building
FROM departments
WHERE building IN (1, 3, 8, 10);
-- 14. Вивести назви захворювань усіх ступенів тяжкості,
-- крім 1-го та 2-го.
SELECT name
FROM diseases
WHERE severity NOT IN (1, 2);
-- 15. Вивести назви відділень, які не знаходяться у
-- першому або третьому корпусі.
SELECT name
FROM departments
WHERE building NOT IN (1, 3);
-- 16. Вивести назви відділень, які знаходяться у першому
-- або третьому корпусі.
SELECT name
FROM departments
WHERE building IN (1, 3);
-- 17. Вивести прізвища лікарів, що починаються з літери
-- «N».
SELECT surname
FROM doctors
WHERE surname ILIKE 'N%';

-- number of wards in each building
SELECT building, COUNT(*) AS "wards num"
FROM wards
GROUP BY building;

-- wards per floor
SELECT floor, COUNT(*) AS "wards num"
FROM wards
GROUP BY floor;

-- average financing for every building
SELECT building, AVG(financing) AS "avg financing"
FROM departments
GROUP BY building

-- max financing per building
SELECT building, MAX(financing) as "max financing"
FROM departments
GROUP BY building;

-- min financing per building
SELECT building, MIN(financing) as "max financing"
FROM departments
GROUP BY building;

-- Вивести загальну суму фінансування для кожного корпусу.
SELECT building, SUM(financing)
FROM departments
GROUP BY building

-- Вивести кількість відділень у кожному корпусі.

SELECT building, COUNT(name)
FROM departments
GROUP BY building

-- Вивести кількість захворювань для кожного ступеня тяжкості.

SELECT severity, COUNT(*) AS "number of cases"
FROM diseases
GROUP BY severity

-- Вивести середню зарплату лікарів залежно від наявності телефону.

SELECT
    (PHONE IS NOT NULL) AS "Має телефон",
    ROUND(AVG(SALARY), 2) AS "Середня зарплата"
FROM DOCTORS
GROUP BY (PHONE IS NOT NULL);

-- Вивести кількість обстежень для кожного дня тижня.
SELECT day_of_week, COUNT(*) "num of examinations"
FROM EXAMINATIONS
GROUP BY day_of_week
ORDER BY day_of_week

-- Вивести найраніший час початку обстежень для кожного дня тижня.

SELECT day_of_week, MIN(start_time) AS "start time"
FROM examinations
GROUP BY day_of_week

-- latest end_time
SELECT day_of_week, MAX(end_time) AS "end time"
FROM examinations
GROUP BY day_of_week

-- Вивести кількість лікарів із зарплатою понад 2000 у кожному корпусі.

SELECT department_id, COUNT(*)
FROM doctors
WHERE salary > 30000
GROUP BY department_id

-- biggest sallary
SELECT SURNAME, SALARY
FROM DOCTORS
WHERE SALARY = (
	SELECT MAX(SALARY)
	FROM DOCTORS
)

-- MIN SALARY

SELECT SURNAME, SALARY
FROM DOCTORS
WHERE SALARY = (
	SELECT MIN(SALARY)
	FROM DOCTORS
)

-- EARLIEST EXAMINATION

SELECT NAME, START_TIME AS EARLIEST_EXAMINATION
FROM EXAMINATIONS
WHERE START_TIME = (
	SELECT MIN(START_TIME)
	FROM EXAMINATIONS
)

--

SELECT NAME, END_TIME AS LATEST_EXAMINATION_FINISH
FROM EXAMINATIONS
WHERE END_TIME = (
	SELECT MAX(END_TIME)
	FROM EXAMINATIONS
)
