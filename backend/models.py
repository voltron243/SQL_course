# Each model should be a class. 
# This package is used to create a class for this database
from sqlalchemy import Column, Date, ForeignKey, Integer, String, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship 


Base = declarative_base()

# Import declarative_base package to create class for model definitions
class Student(Base):  # Base is an instance from the 
    """"
    Student Table  
    """
    
    __tablename__ = 'Student'
    
    Student_ID = Column(Integer, primary_key=True, autoincrement=True, comment='Student_ID') # Column itself is an int
    Student_name = Column(String(100), nullable=False, comment='Student Name') # Column itself is a string
    Gender = Column(String(50), nullable=False, comment='Gender') 
    Age = Column(Integer, nullable=False)
    Class_ = Column('Class', String(100), nullable=False)
    
    # Relationship from Enrollment 
    # Through the enrollment form (see which student has enrolled)
    Enrollment = relationship('Enrollment', back_populates='Student')
    
    # We need to define dictionary - We need to return a dictionary that we found in the database
    # A dictionary can be a database
    def to_dict(self):
        return{
            'Student_ID': self.Student_ID,
            'Student_name': self.Student_name, 
            'Gender': self.Gender,
            'Age': self.Age,
            'Class': self.Class_
        }
        
# Teacher Table 
class Teacher(Base):
    """"
    Teacher Table. 
    """
    
    __tablename__ = 'Teacher'
    
    Teacher_ID = Column(Integer, primary_key=True, autoincrement=True) 
    Teacher_name = Column (String(50), nullable=False, comment='Teacher_name')
    Title = Column(String(100), nullable=False, comment='Title')
    Department = Column(String(100), nullable=False, comment='Department')

    # Relationship statement related to the course table
    Course = relationship('Course', back_populates='Teacher')
    
    def to_dict(self):
        return{
            'Teacher_ID': self.Teacher_ID,
            'Teacher_name': self.Teacher_name,
            'Title': self.Title, 
            'Department': self.Department
        }
 
 # Course Table
class Course(Base):
    """
    Course Table 
    """
    
    __tablename__ = 'Course'
    
    Course_ID = Column(Integer, primary_key=True, autoincrement=True, comment='Course_ID')
    Course_name = Column(String(100), nullable=False, comment='Course_name')
    Credits = Column(Integer, nullable=False, comment='Credits')
    Teacher_ID = Column(Integer, ForeignKey('Teacher.Teacher_ID'))
    
    # Relationship statement related to the teacher table
    # In the relationship, it will return everything from the table 
    Teacher = relationship('Teacher', back_populates='Course')
    Enrollment =  relationship('Enrollment', back_populates='Course')
    
    def to_dict(self):
        return{
            'Course_ID': self.Course_ID,
            'Course_name': self.Course_name,
            'Credits': self.Credits,
            'Teacher_ID': self.Teacher_ID,
            'Teacher_name': self.Teacher.Teacher_name if self.Teacher else None
        }

# Enrollment Table
# If there is no relationship, then put none
class Enrollment(Base):
    """"
    Enrollment Table
    """  
    
    __tablename__ = 'Enrollment'
    
    Enrollment_ID = Column(Integer, primary_key=True, autoincrement=True, comment='Enrollment_ID')
    Student_ID = Column(Integer, ForeignKey('Student.Student_ID'), nullable=False)
    Course_ID = Column(Integer, ForeignKey('Course.Course_ID'), nullable=False)
    Score = Column(String(50), nullable=False, comment='Score')
    Enrollment_date = Column(Date, comment='Enrollment_date')
    
    # Relationship
    Student = relationship('Student', back_populates='Enrollment') 
    Course = relationship('Course', back_populates='Enrollment')
    
    def to_dict(self):
        return{
            'Enrollment_ID': self.Enrollment_ID,
            'Score': self.Score,
            'Enrollment_date': self.Enrollment_date, # % mark is to be changed for the numbers 
            'Student_ID': self.Student_ID,
            'Student_name': self.Student.Student_name if self.Student else None,
            'Course_ID': self.Course_ID,
            'Course_name': self.Course.Course_name if self.Course else None
        }
    
     
        

        

    