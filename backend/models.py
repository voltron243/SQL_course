# Each model should be a class. 
# This package is used to create a class for this database
from sqlalchemy import Column, Integer, String, true
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# Import declarative_base package to create class for model definitions
class Student(Base):  # Base is an instance from the 
    """"
    Student Table  
    """
    
    __tablename__ = 'Student'
    
    Student_ID = Column(Integer, primary_key=True, autoincrement=True) # Column itself is an int
    Student_name = Column(String(50), nullable=False, comment='Student Name')
    Gender = Column(String(50), nullable=False, comment='Gender')
    Age = Column(Integer, nullable=False)
    Class_ = Column('class', String(100), nullable=False)
    
    # We need to define dictionary - We need to return a dictionary that we found in the database
    # A dictionary can be a data
    def to_dict(self):
        return{
            'Student_ID': self.Student_ID,
            'Student_name': self.Student_name, 
            'Gender': self.Gender,
            'Age': self.Age,
            'Class': self.Class_
        }
    
    # single-column comments 
    """
    Multi-column comments 
    """
    
    '''
    Multi-column comments 
    ''' 