SELECT IF(grades.grade > 7, students.name, NULL), grades.grade, students.marks
FROM students
INNER JOIN grades
ON students.marks BETWEEN Min_Mark AND Max_Mark
ORDER BY grades.grade DESC, students.name, students.marks;
