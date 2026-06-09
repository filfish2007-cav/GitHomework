-- 1. Усі можливі пари рядків викладачів і груп

SELECT * FROM teachers
CROSS JOIN groups;

-- 2. Назви факультетів, фонд фінансування кафедр яких перевищує фонд фінансування факультету

SELECT f.name
FROM faculties f
JOIN departments d ON d.faculty_id = f.id
GROUP BY f.id, f.name, f.financing
HAVING SUM(d.financing) > f.financing;

-- 3. Прізвища кураторів груп і назви груп, які вони курирують

SELECT c.surname AS curator_surname, g.name AS group_name
FROM groups_curators gc
JOIN curators c ON gc.curator_id = c.id
JOIN groups g ON gc.group_id = g.id;

-- 4. Імена та прізвища викладачів, які читають лекції у групі «P107»

SELECT DISTINCT t.name, t.surname
FROM teachers t
JOIN lectures l ON l.teacher_id = t.id
JOIN groups_lectures gl ON gl.lecture_id = l.id
JOIN groups g ON gl.group_id = g.id
WHERE g.name = 'P107';

-- 5. Прізвища викладачів і назви факультетів, на яких вони читають лекції

SELECT DISTINCT t.surname, f.name AS faculty_name
FROM teachers t
JOIN lectures l ON l.teacher_id = t.id
JOIN groups_lectures gl ON gl.lecture_id = l.id
JOIN groups g ON gl.group_id = g.id
JOIN departments d ON g.department_id = d.id
JOIN faculties f ON d.faculty_id = f.id;

-- 6. Назви кафедр і назви груп, які до них належать


SELECT d.name AS department_name, g.name AS group_name
FROM departments d
JOIN groups g ON g.department_id = d.id;

-- 7. Назви предметів, які викладає викладач «Samantha Adams»

SELECT DISTINCT s.name
FROM subjects s
JOIN lectures l ON l.subject_id = s.id
JOIN teachers t ON l.teacher_id = t.id
WHERE t.name = 'Samantha' AND t.surname = 'Adams';

-- 8. Назви кафедр, на яких викладається дисципліна «Database Theory»

SELECT DISTINCT d.name
FROM departments d
JOIN groups g ON g.department_id = d.id
JOIN groups_lectures gl ON gl.group_id = g.id
JOIN lectures l ON gl.lecture_id = l.id
JOIN subjects s ON l.subject_id = s.id
WHERE s.name = 'Database Theory';

-- 9. Назви груп, що належать до факультету «Computer Science»

SELECT g.name
FROM groups g
JOIN departments d ON g.department_id = d.id
JOIN faculties f ON d.faculty_id = f.id
WHERE f.name = 'Computer Science';

-- 10. Назви груп 5-го курсу, а також назви факультетів, до яких вони належать

SELECT g.name AS group_name, f.name AS faculty_name
FROM groups g
JOIN departments d ON g.department_id = d.id
JOIN faculties f ON d.faculty_id = f.id
WHERE g.year = 5;

-- 11. Повні імена викладачів і лекції, які вони читають в аудиторії «B103»

SELECT t.name || ' ' || t.surname AS teacher_full_name, s.name AS subject_name, g.name AS group_name
FROM teachers t
JOIN lectures l ON l.teacher_id = t.id
JOIN subjects s ON l.subject_id = s.id
JOIN groups_lectures gl ON gl.lecture_id = l.id
JOIN groups g ON gl.group_id = g.id
WHERE l.lecture_room = 'B103';
