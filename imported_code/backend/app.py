# Flask Application Main File

from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import MYSQL_CONFIG, FLASK_CONFIG
from routes import init_routes
from models import Base

# Create Flask application
app = Flask(__name__)

CORS(app)

# Create database connection

DATABASE_URL = f"mysql+pymysql://{MYSQL_CONFIG['user']}:{MYSQL_CONFIG['password']}@{MYSQL_CONFIG['host']}:{MYSQL_CONFIG['port']}/{MYSQL_CONFIG['database']}?charset={MYSQL_CONFIG['charset']}"

engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

# Initialize routes
init_routes(app, SessionLocal)

# Define a simple route for testing
@app.route('/')
def index():
    return {
        'message': 'Student Management System API',
        'status': 'running',
        'version': '1.0',
        'endpoints': {
            'students': '/api/students',
            'teachers': '/api/teachers',
            'courses': '/api/courses',
            'enrollments': '/api/enrollments'
        }
    }

# Start the Flask application
if __name__ == '__main__':
    # Create all tables (if they don't exist)
    try:
        Base.metadata.create_all(engine)
        print("Database tables created successfully")
    except Exception as e:
        print(f"Database table creation failed: {e}")

    # Start Flask application
    host = FLASK_CONFIG['host']
    port = FLASK_CONFIG['port']
    
    if host == '0.0.0.0':
        print(f"Flask server started at http://localhost:{port}")
        print(f"Or access via: http://127.0.0.1:{port}")
    else:
        print(f"Flask server started at http://{host}:{port}")
    
    app.run(
        host=host,
        port=port,
        debug=FLASK_CONFIG['debug']
    )
