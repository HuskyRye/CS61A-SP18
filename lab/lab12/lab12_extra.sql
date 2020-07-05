.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT s1.date, s1.color, s1.pet, s1.number, s2.number
  FROM students as s1, fa17students as s2
  WHERE s1.date = s2.date and s1.color = s2.color and s1.pet = s2.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT seven
  FROM students, checkboxes
  WHERE students.time = checkboxes.time and number = 7 and "7" = "True";

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, COUNT(*) AS count
  FROM fa17students GROUP BY number
  ORDER BY count DESC LIMIT 1;


CREATE TABLE fa17favpets AS
  SELECT pet, COUNT(*) AS count
  FROM fa17students GROUP BY pet
  ORDER BY count DESC, pet LIMIT 10;


CREATE TABLE sp18favpets AS
  SELECT pet, COUNT(*) AS count
  FROM students GROUP BY pet
  ORDER BY count DESC, pet LIMIT 10;


CREATE TABLE sp18dog AS
  SELECT pet, COUNT(*) As count
  FROM students
  WHERE pet = "dog";


CREATE TABLE sp18alldogs AS
  SELECT pet, COUNT(*) As count
  FROM students
  WHERE pet LIKE "%dog%";


CREATE TABLE obedienceimages AS
  SELECT seven, denero, COUNT(*)
  FROM students
  WHERE seven = "7"
  GROUP BY denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) As count
  FROM students GROUP BY smallest
  ORDER BY smallest;
