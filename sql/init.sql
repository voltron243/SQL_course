CREATE DATABASE IF NOT EXISTS sql_course DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE sql_course;

-- Student's table 
CREATE TABLE IF NOT EXISTS `Student`(
    `Student_ID` INT PRIMARY KEY AUTO_INCREMENT,
    `Student_name` VARCHAR(100) NOT NULL,
    `Gender` CHAR(50) NOT NULL,
    `Age` int NOT NULL,
    `Class` VARCHAR(100) NOT NULL
);

-- Teacher's table
CREATE TABLE IF NOT EXISTS `Teacher`(
    `Teacher_ID` INT PRIMARY KEY AUTO_INCREMENT,
    `Teacher_name` VARCHAR(50) NOT NULL,
    `Title` VARCHAR(100) NOT NULL,
    `Department` VARCHAR(100) NOT NULL
);

-- Course's table
CREATE TABLE IF NOT EXISTS `Course`(
    `Course_ID` INT PRIMARY KEY AUTO_INCREMENT,
    `Course_name` VARCHAR(100) NOT NULL,
    `Credits` INT NOT NULL,
    `Teacher_ID` INT NOT NULL,
    FOREIGN KEY (Teacher_ID) REFERENCES Teacher(Teacher_ID)
);

-- Enrollment's table 
CREATE TABLE IF NOT EXISTS `Enrollment`(
    `Enrollment_ID` INT PRIMARY KEY AUTO_INCREMENT,
    `Student_ID` INT NOT NULL,
    `Course_ID` INT NOT NULL,
    `Score` VARCHAR(50) NOT NULL, -- List to do rank (Better to use INT) PYTHON CAN CONVERT STRING TO INT
    `Enrollment_date` INT, 
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID), -- FOREIGN KEY HAS TO BE LAST
    FOREIGN KEY (Course_ID) REFERENCES  Course(Course_ID),
    unique(Student_ID, Course_ID)
);

-- Inserting the records
-- Inserting records for the "Student table"
INSERT INTO `Student` (`Student_ID`, `Student_name`, `Gender`, `Age`, `Class`) 
VALUES
    ('10011', 'Student_A', 'Male', '20', 'Computer Science'),
    ('20022', 'Student_B', 'Female', '21', 'Statistics'),
    ('30033', 'Student C', 'Male', '23', 'Computer Science'),
    ('40044', 'Student D', 'Male', '22', 'Engineering'),
    ('50055', 'Student E', 'Female', '20', 'Architecture'),
    ('60066', 'Student F', 'Female', '23', 'Architecture'),
    ('70077', 'Student G', 'Female', '20', 'Science'),
    ('80088', 'Student H', 'Male', '21', 'Urban Planning'),
    ('90099', 'Student I', 'Female', '24', 'Calculus'),
    ('100000', 'Student J', 'Male', '22', 'Computer Science');    

-- Inserting records for the "Teacher table"
INSERT INTO `Teacher` (`Teacher_ID`, `Teacher_name`, `Title`, `Department`)
VALUES
    ('3492', 'Teacher A', 'Professor', 'Faculty of Engineering and Design'),
    ('4365', 'Teacher B', 'Professor', 'Faculty of Science'),
    ('2675', 'Teacher C', 'Professor', 'Faculty of Engineering and Design'),
    ('2645', 'Teacher D', 'Professor', 'Faculty of Science'),
    ('6035', 'Teacher E', 'Professor', 'Faculty of Science'),
    ('2971', 'Teacher F', 'Professor', 'Faculty of Engineering and Design'),
    ('2576', 'Teacher G', 'Professor', 'Faculty of Engineering and Design'),
    ('5710', 'Teacher H', 'Professor', 'Faculty of Engineering and Design'),
    ('8700', 'Teacher I', 'Professor', 'Faculty of Science'),
    ('4761', 'Teacher J', 'Professor', 'Faculty of Science');     

-- Inserting records for the "Course table"
INSERT INTO `Course` (`Course_ID`, `Course_name`, `Credits`, `Teacher_ID`)
VALUES
    ('472', 'Computer Science', '6', '3492'), 
    ('860', 'Architecture', '4', '4365'),
    ('255', 'Computer Science', '10', '2675'),
    ('321', 'Urban Planning', '10', '2645'),
    ('669', 'Computer Science', '3', '6035'),
    ('965', 'Architecture', '5', '2971'),
    ('758', 'Urban Planning', '12', '2576'),
    ('842', 'Computer Science', '6', '8700'),
    ('894', 'Urban Planning', '14', '5710'),
    ('948', 'Architecture', '10', '4761');  
    
-- Inserting records for the "Enrollment table"
INSERT INTO `Enrollment` (`Student_ID`, `Course_ID`, `Score`)
VALUES
    ('10011', '472', 'A+'),
    ('20022', '860', 'A+'),
    ('30033', '255', 'A'),
    ('40044', '321', 'B+'),
    ('50055', '669', 'B-'),
    ('60066', '965', 'A-'),
    ('70077', '758', 'A'),
    ('80088', '842', 'A+'),
    ('90099', '894', 'B'),
    ('100000', '948', 'B');  

-- Sorting the tables 
-- Sorting the "Student table" 
SELECT * FROM `sql_course`.`Student`
ORDER BY `Age` ASC;  -- From youngest to oldest for age 

-- Sorting the "Teacher table"
SELECT * FROM `sql_course`.`Teacher`
ORDER BY `Teacher_ID` ASC; -- From smallest to biggest for teacher_ID








