# Database Model Definitions

from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Student(Base):
    """Student Table"""
    __tablename__ = 'Student'
    
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(50), nullable=False, comment='Student Name')
    gender = Column(String(10), comment='Gender')
    age = Column(Integer, comment='Age')
    class_ = Column('class', String(50), comment='Class')
    
    # Relationships
    enrollments = relationship('Enrollment', back_populates='student')

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'student_name': self.student_name,
            'gender': self.gender,
            'age': self.age,
            'class': self.class_
        }


class Teacher(Base):
    """Teacher Table"""
    __tablename__ = 'Teacher'
    
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_name = Column(String(50), nullable=False, comment='Teacher Name')
    title = Column(String(50), comment='Title')
    department = Column(String(50), comment='Department')
    
    # Relationships
    courses = relationship('Course', back_populates='teacher')

    def to_dict(self):
        return {
            'teacher_id': self.teacher_id,
            'teacher_name': self.teacher_name,
            'title': self.title,
            'department': self.department
        }


class Course(Base):
    """Course Table"""
    __tablename__ = 'Course'
    
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(50), nullable=False, comment='Course Name')
    credits = Column(Integer, comment='Credits')
    teacher_id = Column(Integer, ForeignKey('Teacher.teacher_id'), comment='Teacher ID')
    
    # Relationships
    teacher = relationship('Teacher', back_populates='courses')
    enrollments = relationship('Enrollment', back_populates='course')

    def to_dict(self):
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'credits': self.credits,
            'teacher_id': self.teacher_id,
            'teacher_name': self.teacher.teacher_name if self.teacher else None
        }


class Enrollment(Base):
    """Enrollments Table"""
    __tablename__ = 'Enrollments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('Student.student_id'), nullable=False, comment='Student ID')
    course_id = Column(Integer, ForeignKey('Course.course_id'), nullable=False, comment='Course ID')
    score = Column(DECIMAL(5, 2), comment='Score')
    enroll_date = Column(Date, comment='Enrollment Date')
    
    # Relationships
    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'student_name': self.student.student_name if self.student else None,
            'course_id': self.course_id,
            'course_name': self.course.course_name if self.course else None,
            'score': float(self.score) if self.score else None,
            'enroll_date': self.enroll_date.strftime('%Y-%m-%d') if self.enroll_date else None
        }



class User(Base):
    """User Table"""
    __tablename__ = 'User'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True, comment='Username')
    password = Column(String(100), nullable=False, comment='Password')
    email = Column(String(100), nullable=False, comment='Email')

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email
        }
