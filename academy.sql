-- 1. Пошук високооплачуваних викладачів (Таблиця Teachers)
SELECT Surname, Name, Position, Salary
FROM Teachers
WHERE Salary > '20000.00' OR IsProfessor = TRUE;
-- 2. Фільтрація кафедр за бюджетом (Таблиця Departments)
SELECT Name, Financing
FROM Departments
WHERE Financing > '150000.00'
ORDER BY Financing DESC;
-- 3. Пошук успішних груп старших курсів (Таблиця Groups)
SELECT Name, Rating, Year
FROM Groups
WHERE Year >= 3 AND Rating IN (4, 5);
-- 4. Аналіз молодих кадрів (Таблиця Teachers)
SELECT Surname, Name, EmploymentDate, IsAssistant
FROM Teachers
WHERE IsAssistant = TRUE AND EmploymentDate >= '2020-01-01';
-- 5. Пошук деканського складу факультетів (Таблиця Faculties)
SELECT Name, Dean
FROM Faculties
WHERE Dean LIKE 'проф. С%' OR Name LIKE '%комп''ютерних%';
