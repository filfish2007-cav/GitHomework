-- 1. ПІБ студентів з мінімальною оцінкою у вказаному діапазоні
-- Використовуємо стовпець min_grade та оператор BETWEEN.
SELECT full_name
FROM student_grades
WHERE min_grade BETWEEN 3 AND 5;

-- 2. Інформація про студентів, яким виповнилося 20 років
-- Для точного розрахунку віку на поточну дату використовуємо функцію AGE().
SELECT * FROM student_grades
WHERE EXTRACT(YEAR FROM AGE(CURRENT_DATE, birth_date)) = 20;

-- 3. Інформація про студентів з віком у вказаному діапазоні
-- Обчислюємо вік через AGE() та фільтруємо через BETWEEN.

SELECT * FROM student_grades
WHERE EXTRACT(YEAR FROM AGE(CURRENT_DATE, birth_date)) BETWEEN 7 AND 10;

-- 4. Інформація про студентів із конкретним ім’ям (наприклад, Борис)
-- Оскільки в таблиці є стовпець full_name (де зазвичай зберігається Прізвище + Ім'я), використовуємо оператор LIKE або ILIKE (регістронезалежний), щоб знайти ім'я всередині рядка.
SELECT * FROM student_grades
WHERE full_name ILIKE '%Борис%';

-- 5. Інформація про студентів, в номері телефону яких є три сімки
-- Шукаємо підрядок 777 у стовпці phone за допомогою маски %777%.
SELECT * FROM student_grades
WHERE phone LIKE '%777%';

-- 6. Електронні адреси студентів, що починаються з конкретної літери (наприклад, 'A')
-- Використовуємо маску A% (символ % означає будь-яку кількість символів після літери). ILIKE забезпечить пошук як великої 'A', так і малої 'a'.
SELECT email
FROM student_grades
WHERE email ILIKE 'A%';

-- 8. Мінімальна середня оцінка по всіх студентах
-- Використовуємо стовпець gpa_yearly (річний середній бал).

SELECT MIN(gpa_yearly) AS min_overall_gpa
FROM student_grades;

-- 9. Максимальна середня оцінка по всіх студентах

SELECT MAX(gpa_yearly) AS max_overall_gpa
FROM student_grades;

-- 10. Статистика міст (назва міста та кількість студентів)
-- Групуємо дані за стовпцем city за допомогою GROUP BY.

SELECT city, COUNT(*) AS student_count
FROM student_grades
GROUP BY city
ORDER BY student_count DESC;

-- 11. Статистика країн (назва країни та кількість студентів)
-- Групуємо дані за стовпцем country.
SELECT country, COUNT(*) AS student_count
FROM student_grades
GROUP BY country
ORDER BY student_count DESC;

-- 12. Кількість студентів з мінімальною оцінкою з математики
-- Запит розраховує, яка оцінка в таблиці є найменшою серед усіх для предмета 'Математика' (або подібного), а потім рахує кількість студентів, що мають саме цю оцінку.
-- Примітка: Оскільки в структурі вашої таблиці назва предмета міститься в текстових полях типу min_grade_subject, фільтруємо за назвою предмета.

SELECT COUNT(*) AS students_with_min_math_grade
FROM student_grades
WHERE min_grade_subject ILIKE '%математика%'
  AND min_grade = (
      SELECT MIN(min_grade)
      FROM student_grades
      WHERE min_grade_subject ILIKE '%математика%'
  );

-- 13. Кількість студентів з максимальною оцінкою з математики
SELECT COUNT(*) AS students_with_max_math_grade
FROM student_grades
WHERE max_grade_subject ILIKE '%математика%'
  AND max_grade = (
      SELECT MAX(max_grade)
      FROM student_grades
      WHERE max_grade_subject ILIKE '%математика%'
  );

-- 14. Кількість студентів у кожній групі
-- Групуємо за стовпцем group_name.

SELECT group_name, COUNT(*) AS total_students
FROM student_grades
GROUP BY group_name
ORDER BY group_name;

-- 15. Середня оцінка групи
-- Вираховуємо середнє значення (AVG) річного бала gpa_yearly для кожної групи окремо.

SELECT group_name, ROUND(AVG(gpa_yearly), 2) AS average_group_gpa
FROM student_grades
GROUP BY group_name
ORDER BY average_group_gpa DESC;
