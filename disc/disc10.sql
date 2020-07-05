CREATE TABLE records AS
SELECT "Alyssa P Hacker" AS Name, "Computer" AS Division, "Programmer" AS Title, 40000 AS Salary, "Ben Bitdiddle" AS Supervisor UNION
SELECT "Ben Bitdiddle"          , "Computer"            , "Wizard"             , 60000          , "Oliver Warbucks"             UNION
SELECT "Cy D Fect"              , "Computer"            , "Programmer"         , 35000          , "Ben Bitdiddle"               UNION
SELECT "Eben Scrooge"           , "Accounting"          , "Chief Accountant"   , 75000          , "Oliver Warbucks"             UNION
SELECT "Lem E Tweakit"          , "Computer"            , "Technician"         , 25000          , "Ben Bitdiddle"               UNION
SELECT "Louis Reasoner"         , "Computer"            , "Programmer Trainee" , 30000          , "Alyssa P Hacker"             UNION
SELECT "Oliver Warbucks"        , "Administration"      , "Big Wheel"          , 150000         , "Oliver Warbucks"             UNION
SELECT "Robert Cratchet"        , "Accounting"          , "Scrivener"          , 18000          , "Eben Scrooge";

/*
SELECT name FROM records WHERE supervisor = "Oliver Warbucks";
SELECT * FROM records WHERE name = supervisor;
SELECT name FROM records WHERE salary > 50000 ORDER BY name;
*/

CREATE TABLE meetings AS
SELECT "Accounting" AS Division, "Monday" AS Day, "9am" as Time UNION
SELECT "Computer"              , "Wednesday"    , "4pm"         UNION
SELECT "Administration"        , "Monday"       , "11am"        UNION
SELECT "Administration"        , "Thursday"     , "1pm";

CREATE TABLE earn_more AS
SELECT r1.name, r1.salary, r2.name, r2.salary
FROM records AS r1, records AS r2
WHERE r1.supervisor = r2.name AND r2.salary > r1.salary * 2;

CREATE TABLE different_division AS
SELECT r1.name
FROM records AS r1, records AS r2
WHERE r1.supervisor = r2.name AND r1.Division != r2.Division;

/* Write a query that outputs the meeting days and times of all employees directly
   supervised by Oliver Warbucks. */
CREATE TABLE "3.3" AS
SELECT day, time FROM records, meetings
WHERE records.division = meetings.division AND supervisor = "Oliver Warbucks";

CREATE TABLE middle_manager AS
SELECT DISTINCT r2.name FROM records AS r1, records AS r2, records AS r3
WHERE r1.supervisor = r2.name and r2.supervisor = r3.name and r2.supervisor != r2.name;

CREATE TABLE same_day AS
SELECT r1.name
FROM records AS r1, meetings AS m1, records AS r2, meetings AS m2
WHERE r1.supervisor = r2.name AND r1.division = m1.division AND r2.division = m2.division
		AND r1.supervisor != r1.name AND m1.day = m2.day;
		
CREATE TABLE dogs(name, age, phrase DEFAULT "woof");
INSERT INTO dogs(name, age) VALUES ("Fido", 1), ("Sparky", 2);
INSERT INTO dogs VALUES ("Lassie", 2, "I'll save you!"), ("Floofy", 3, "Much doge");
-- UPDATE dogs SET age = age+1;

CREATE TABLE courses AS
SELECT "John DeNero" AS Professor, "CS 61A" AS Course, "Fa17" AS Semester UNION
SELECT "Paul Hilfinger"          , "CS 61A"          , "Fa17"             UNION
SELECT "Paul Hilfinger"          , "CS 61A"          , "Sp17"             UNION
SELECT "John DeNero"             , "Data 8"          , "Sp17"             UNION
SELECT "Josh Hug"                , "CS 61B"          , "Sp17"             UNION
SELECT "Satish Rao"              , "CS 70"           , "Sp17"             UNION
SELECT "Nicholas Weaver"         , "CS 61C"          , "Sp17"             UNION
SELECT "Gerald Friedland"        , "CS 61C"          , "Sp17"             UNION
SELECT "John DeNero"             , "CS 61A"          , "Fa16"             UNION
SELECT "Paul Hilfinger"          , "CS 61B"          , "Fa16";

CREATE TABLE num_taught AS
SELECT "Gerald Friedland" AS Professor, "CS 61C" AS Course, 1 AS Times UNION
SELECT "John DeNero"                  , "CS 61A"          , 2          UNION
SELECT "John DeNero"                  , "Data 8"          , 1          UNION
SELECT "Josh Hug"                     , "CS 61B"          , 1          UNION
SELECT "Nicholas Weaver"              , "CS 61C"          , 1          UNION
SELECT "Paul Hilfinger"               , "CS 61A"          , 2          UNION
SELECT "Paul Hilfinger"               , "CS 61B"          , 1          UNION
SELECT "Satish Rao"                   , "CS 70 "          , 1;

SELECT Course FROM num_taught WHERE Professor = "Paul Hilfinger";

SELECT courses.* FROM courses, num_taught
WHERE courses.Professor = num_taught.Professor AND courses.Course = num_taught.Course AND num_taught.Times > 1;

SELECT n1.Professor, n2.Professor, n1.Course FROM num_taught AS n1, num_taught AS n2
WHERE n1.Course = n2.Course AND n1.Times = n2.Times AND n1.Professor < n2.Professor;
