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
    `Course_ID` INT NOT NULL  PRIMARY KEY AUTO_INCREMENT,
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
    ('100', 'Student_A', 'Male', '20', 'Computer Science'),
    ('200', 'Student_B', 'Female', '21', 'Statistics'),
    ()
    ()
    ()
    ()
    ()
    ()
    ()
    ();    

-- Inserting records for the "Teacher table"
INSERT INTO `Teacher` (`Teacher_ID`, `Course_name`, `Title`, `Department`)
VALUES
    ()
    ()
    ()
    ()
    ()
    ()
    ()
    ()
    ()
    ();     

-- Inserting records for the "Course table"
INSERT INTO `Course` (`Course_ID`, `Course_name`, `Credits`, `Teacher_ID`)
VALUES
    ()
    ()
    ()
    ()
    ()
    ()
    ()
    ()
    ()
    ();  

-- Inserting records for the "Enrollment table"
INSERT INTO `Enrollment` (`Enrollment_ID`, `Student_ID`, `Course_ID`, `Score`, `Enrollment_date`)
VALUES
    ()
    ()
    ()
    ()
    ()
    ()
    ()
    ()
    ()
    ();  

-- Sorting the tables 
-- Sorting the "Student table" 
SELECT * FROM `sql_course`, `student`,
ORDER BY `Age` ASC;  -- From youngest to oldest for age 




