CREATE DATABASE IF NOT EXISTS sql_course_course DEFAULTEN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE sql_course;

-- Student's table 
CREATE TABLE `Student`(
    `Student_ID` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `Student name` VARCHAR(100) NOT NULL,
    `Gender` CHAR(50) NOT NULL,
    `Age` int NOT NULL,
    `Class` VARCHAR(100) NOT NULL;
)

-- Teacher's table
CREATE TABLE `Teacher`(
    `Teacher_ID` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `Teacher_name` VARCHAR(50) NOT NULL,
    `Title` VARCHAR(100) NOT NULL,
    `Department` VARCHAR(100) NOT NULL;
)

-- Course's table
CREATE TABLE `Course`(
    `Course_ID` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `Course_name` VARCHAR(100) NOT NULL,
    `Credits` INT NOT NULL,
    `Teacher_ID` INT NOT NULL,
    FOREIGN KEY (Teacher_ID) REFERENCES Teacher(Teacher_ID);
)

-- Enrollment's table 
CREATE TABLE `Enrollment`(
    `Enrollment_ID` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES  Course(Course_ID),
    `Score` INT NOT NULL, 
    `Enrollment_date` INT NOT NULL, 
    unique(Student_ID, Course_ID);
)

-- Inserting the records
-- Inserting records for the "Student table"
INSERT INTO `Student` (`Student_ID`, `Student_name`, `Gender`, `Age`, `Class`) 
VALUES
    ('10011', 'Student_A', 'Male', '20', 'Computer Science'),
    ('20022', 'Student_B', 'Female', '21', 'Statistics'),
    ('30033', 'Student C', 'Male', '23', 'Computer Science').
    ('40044', 'Student D', 'Male', '22', 'Engineering'),
    ('50055', 'Student E', 'Female', '20', 'Architecture'),
    ('60066', 'Student F', 'Female', '23', 'Architecture'),
    ('70077', 'Student G', 'Female', '20', 'Science'),
    ('80088', 'Student H', 'Male', '21', 'Urban Planning'),
    ('90099', 'Student I', 'Female', '24', 'Calculus'),
    ('100000', 'Student J', 'Male', '22', 'Computer Science');    

-- Inserting records for the "Teacher table"
INSERT INTO `Teacher` (`Teacher_ID`, `Course_name`, `Title`, `Department`)
VALUES
    ('3492', 'Teacher A', 'Architecture', 'Professor', 'Faculty of Engineering and Design'),
    ('4365', 'Teacher B', 'Computer Science', 'Professor', 'Faculty of Science'),
    ('2675', 'Teacher C', 'Urban Planning', 'Professor', 'Faculty of Engineering and Design'),
    ('2675', 'Teacher D', 'Statistics', 'Professor', 'Faculty of Science'),
    ('6035', 'Teacher E', 'Calculus', 'Professor', 'Faculty of Science'),
    ('2971', 'Teacher F', 'Architecture', 'Professor', 'Faculty of Engineering and Design'),
    ('2576', 'Teacher G', 'Engineering', 'Professor', 'Faculty of Engineering and Design'),
    ('5710', 'Teacher H', 'Engineering', 'Professor', 'Faculty of Engineering and Design'),
    ('8700', 'Teacher I', 'Computer Science', 'Professor', 'Faculty of Science'),
    ('4761', 'Teacher J', 'Computer Science', 'Professor', 'Faculty of Science');     

-- Inserting records for the "Course table"
INSERT INTO `Course` (`Course_ID`, `Course_name`, `Credits`, `Teacher_ID`)
VALUES
    ('472', 'Computer Science', '6', ''), -- Question about using the foreign key for Teacher_ID
    ('860', 'Architecture', '4', ''),
    ('255', 'Computer Science', '10', ''),
    ('321', 'Urban Planning', '10', ''),
    ('669', 'Computer Science', '3', ''),
    ('965', 'Architecture', '5', ''),
    ('758', 'Urban Planning', '12', ''),
    ('842', 'Computer Science', '6', ''),
    ('894', 'Urban Planning', '14', ''),
    ('948', 'Architecture', '10', '');  

-- Inserting records for the "Enrollment table"
INSERT INTO `Enrollment` (`Enrollment_ID`, `Student_ID`, `Course_ID`, `Score`, `Enrollment_date`)
VALUES
    (`Student_ID`, `Course_ID`, `A+`, `Enrollment_date`), -- Same goes with Student_ID and Course_ID
    (`Student_ID`, `Course_ID`, `A+`, `Enrollment_date`),
    (`Student_ID`, `Course_ID`, `A`, `Enrollment_date`),
    (`Student_ID`, `Course_ID`, `B+`, `Enrollment_date`),
    (`Student_ID`, `Course_ID`, `B-`, `Enrollment_date`),
    (`Student_ID`, `Course_ID`, `A_`, `Enrollment_date`),
    (`Student_ID`, `Course_ID`, `A`, `Enrollment_date`),
    (`Student_ID`, `Course_ID`, `A+`, `Enrollment_date`),
    (`Student_ID`, `Course_ID`, `B`, `Enrollment_date`),
    (`Student_ID`, `Course_ID`, `B`, `Enrollment_date`);  

-- Sorting the tables 
-- Sorting the "Student table" 
SELECT * FROM `sql_course`, `Student`,
ORDER BY `Age` ASC;  -- From youngest to oldest for age 

--Sorting the "Teacher table"
SELECT * FROM `sql_course`, `Teacher`,
ORDER BY `Teacher_ID` ASC; -- From smallest to biggest for teacher_ID








