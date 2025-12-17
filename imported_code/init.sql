-- Database Initialization Script

CREATE DATABASE IF NOT EXISTS `SQLCourse` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE `SQLCourse`;

CREATE TABLE `SQLCourse`.`Student` (
    `student_id` INT PRIMARY KEY AUTO_INCREMENT,  -- Primary Key
    `student_name` VARCHAR(50) NOT NULL,
    `gender` VARCHAR(10),
    `age` INT,
    `class` VARCHAR(50)
);

CREATE TABLE `SQLCourse`.`Teacher` (
    `teacher_id` INT PRIMARY KEY AUTO_INCREMENT,  -- Primary Key
    `teacher_name` VARCHAR(50) NOT NULL,
    `title` VARCHAR(50),
    `department` VARCHAR(50)
);

CREATE TABLE `SQLCourse`.`Course` (
    `course_id` INT PRIMARY KEY AUTO_INCREMENT,   -- Primary Key
    `course_name` VARCHAR(50) NOT NULL,
    `credits` INT,
    `teacher_id` INT,                             -- Foreign Key, references Teacher table
    FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
);
  
  
CREATE TABLE `SQLCourse`.`Enrollments` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,          -- Primary Key
    `student_id` INT NOT NULL,                    -- Foreign Key, references Student table
    `course_id` INT NOT NULL,                     -- Foreign Key, references Course table
    `score` DECIMAL(5,2),                         -- Optional field: Score 
    `enroll_date` DATE,                           -- Optional field: Enrollment Date
    FOREIGN KEY (`student_id`) REFERENCES Student(`student_id`),
    FOREIGN KEY (`course_id`) REFERENCES Course(`course_id`),
    UNIQUE KEY (`student_id`, `course_id`)          -- Prevent duplicate enrollments
);


CREATE TABLE `SQLCourse`.`User` (
    `user_id` INT PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(50) NOT NULL UNIQUE,
    `password` VARCHAR(50) NOT NULL,
    `email` VARCHAR(100)
);


-- Insert Test Data

INSERT INTO `SQLCourse`.`Student` (`student_id`, `student_name`, `gender`, `age`, `class`) VALUES
(1, 'AAA', 'M', 20, 'Computer Science'),
(2, 'BBB', 'M', 19, 'Computer Science'),
(3, 'CCC', 'F', 21, 'Computer Science'),
(4, 'DDD', 'M', 20, 'Computer Science'),
(5, 'EEE', 'F', 22, 'Computer Science');


INSERT INTO `SQLCourse`.`Teacher` (`teacher_id`, `teacher_name`, `title`, `department`) VALUES
(1, 'GGG', 'professor', 'School of Computer Science'),
(2, 'HHH', 'professor', 'School of Computer Science'),
(3, 'JJJ', 'lecturer', 'School of Computer Science');


INSERT INTO `SQLCourse`.`Course` (`course_id`, `course_name`, `credits`, `teacher_id`) VALUES
(1, 'Data Structure', 4, 1),
(2, 'Calculus', 5, 2),
(3, 'AI', 3, 3),
(4, 'Algorithm', 4, 1),
(5, 'Database', 3, 1);


INSERT INTO `SQLCourse`.`Enrollments` (`student_id`, `course_id`, `score`) VALUES
(1, 1, 85),
(1, 2, 90),
(1, 3, 88),
(2, 1, 92),
(2, 3, 87),
(3, 2, 78),
(3, 4, 85),
(4, 1, 91),
(4, 5, 89),
(5, 2, 76),
(5, 4, 82),
(5, 5, 88);