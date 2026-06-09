-- 1. Повні імена лікарів та їх спеціалізації
SELECT
    d.name || ' ' || d.surname AS doctor_name,
    s.name AS specialization
FROM doctors d
JOIN doctorsspecializations ds ON d.id = ds.doctor_id
JOIN specializations s ON ds.specialization_id = s.id;

-- 2. Виведіть прізвища та зарплати ( сума ставки та надбавки) лікарів, які не перебувають у відпустці.

SELECT
    surname,
    salary + premium AS total_salary
FROM doctors
WHERE id NOT IN (
    SELECT doctorid
    FROM vacations
    WHERE CURRENT_DATE BETWEEN startdate AND enddate
);

-- 3. Виведіть назви палат , які знаходяться у відділенні «Intensive Treatment».


SELECT w.name AS ward_name
FROM wards w
JOIN departments d ON w.departmentid = d.id
WHERE d.name = 'Кардіологічне відділення';

-- 4 Виведіть назви відділень без повторень, які спонсоруються компанією «Umbrella Corporation».

SELECT DISTINCT d.name AS department_name
FROM departments d
JOIN donations don ON d.id = don.department_id
JOIN sponsors s ON don.sponsor_id = s.id
WHERE s.name = 'Фонд Притули';

-- 5. Виведіть усі пожертвування за останній місяць у ви
-- гляді: відділення, спонсор, сума пожертвування, дата
-- пожертвування.

SELECT
    dep.name AS department,
    s.name AS sponsor,
    don.amount,
    don.donation_date
FROM donations don
JOIN departments dep ON don.department_id = dep.id
JOIN sponsors s ON don.sponsor_id = s.id
WHERE don.donation_date >= CURRENT_DATE - INTERVAL '1 month';

-- 6. Прізвища лікарів та їхні відділення (обстеження у будні дні: Пн-Пт)

SELECT DISTINCT
    d.surname AS doctor_surname,
    dep.name AS department_name
FROM doctors d
JOIN examinations e ON d.id = e.doctorid
JOIN wards w ON e.wardid = w.id
JOIN departments dep ON w.departmentid = dep.id
WHERE EXTRACT(ISODOW FROM e.date) NOT IN (6, 7);

-- 7. Виведіть назви відділень, які отримували пожертву-вання
-- у розмірі понад 100000, із зазначенням їх лікарів.

SELECT DISTINCT
    dep.name AS department_name,
    doc.surname || ' ' || doc.name AS doctor
FROM departments dep
JOIN donations don ON dep.id = don.department_id
JOIN doctors doc ON don.department_id = doc.department_id
WHERE don.amount > 100000


-- 8. Назви відділень, де лікарі не отримують надбавки

SELECT name
FROM departments
WHERE id NOT IN (
    SELECT DISTINCT department_id
    FROM doctors
    WHERE premium > 0
);

-- 9. Отделения и названия заболеваний за последние полгода

SELECT DISTINCT
    dep.name AS department_name,
    dis.name AS disease_name
FROM departments dep
JOIN wards w ON dep.id = w.departmentid
JOIN examinations e ON w.id = e.wardid
JOIN diseases dis ON e.diseaseid = dis.id
WHERE e.date >= CURRENT_DATE - INTERVAL '6 months';
