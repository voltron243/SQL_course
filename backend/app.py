from flask import Flask
from flask_cors import CORS
from config import MYSQL_CONFIG
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import FLASK_CONFIG

from routes import init_routes

# Create a flask application 
app = Flask(__name__)

# Decorating little by little 
# We need to access it 

# Allow the front end to use the domain, the IP address, access the backend resources.
# CORS 
# / is the root URL
CORS(app)

# Database connection (f" - Recognise names in curly brackets)
# Set up the database URL (STRING)
DATABASE_URL = f"mysql+pymysql://{MYSQL_CONFIG['user']}:{MYSQL_CONFIG['password']}@{MYSQL_CONFIG['host']}:{MYSQL_CONFIG['port']}/{MYSQL_CONFIG['database']}?charset{MYSQL_CONFIG['charset']}"

# Establish the connection to the dictionary to config
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine) # Initalise the routes

init_routes(app, SessionLocal) # Initiate the app and sessionlocal

# Define the index page route for the testing 
# / is the root URL
# root path 
# Use function code
# Use the dictionary code
# Key is string - list, tuple, or dictionary
# Dictionary to communicate between the backend and the frontend 
# Format on the backend 
@app.route('/')
def index():
    return {
        'message': 'Welcome to the SQL Course Backend',
        'status': 'success',
        'version': '1.0,0',  
        'data': {
            'Student_ID': 'Student_ID',
            'Student_name': 'Student_name', 
            'Gender': 'Gender',
            'Age': 'Age',
            'Class': 'Class_',
            'Test': 'Test',
            'Teacher_ID': 'Teacher_ID',
            'Teacher_name': 'Teacher_name',
            'Credits':'Credits',
            'Title': 'Title',
            'Department': 'Department',
            'Course_ID': 'Course_ID',
            'Course_name': 'Course_name',
            'Credits': 'Credits',
            'Enrollment_ID': 'Enrollment_ID',
            'Score': 'Score',
            'Enrollment_date': 'Enrollment_date'
        }
    }
    
# Allow the front end to access the visuals in the backend 

# python aplication: Will start to find this if __name__ == '__main__':
# Run the app
if __name__ == '__main__':
    host = FLASK_CONFIG['host']
    port = FLASK_CONFIG['port']
    debug = FLASK_CONFIG['debug']
    
    # If statement 
    # Easier to identify where the error is from
    # f means follow link (Make sure it delivers the value, making the string in dynamic )
    
    if host == '0.0.0.0':
        print(f"Starting server on all interfaces at port {port}...")
    else:
        print(f"Starting server at http://{host}:{port}...")
    
    app.run(
        host=host,
        port=port,
        debug=debug
    )
    
    # That is the minimal setup for the backend 
    
    