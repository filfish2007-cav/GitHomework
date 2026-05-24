-- Відображати всієї інформації з таблиці зі студентами
-- та оцінками.

-- SELECT * FROM student_grades ORDER BY id;

-- Відображати ПІБ усіх студентів.

-- SELECT full_name FROM student_grades;

-- Відображати усіх середніх оцінок.

-- SELECT gpa_yearly FROM student_grades;

-- Показати ПІБ усіх студентів з мінімальною оцінкою,
-- більшою, ніж зазначена.

-- SELECT full_name FROM student_grades WHERE gpa_yearly > 4.1;

-- Показати країни студентів. Назви країн мають бути
-- унікальними.

-- SELECT DISTINCT country FROM student_grades;

-- Показати міста студентів. Назви міст мають бути
-- унікальними.

-- SELECT DISTINCT city FROM student_grades;

-- Показати назви груп. Назви груп мають бути уні-
-- кальними.

-- SELECT DISTINCT group_name FROM student_grades;

-- Показати назви усіх предметів із мінімальними се-
-- редніми оцінками. Назви предметів мають бути уні-
-- кальними.

-- SELECT DISTINCT min_grade_subject FROM student_grades;

-- SELECT full_name FROM student_grades WHERE gpa_yearly BETWEEN 7 AND 9
