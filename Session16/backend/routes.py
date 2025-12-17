# API Route Definitions

from flask import Blueprint, jsonify, request
from sqlalchemy.orm import Session
from models import Student, Teacher, Course, Enrollment, User

api = Blueprint('api', __name__, url_prefix='/api')


def init_routes(app, db_session):
    """Initialize routes"""
    
    @api.route('/students', methods=['GET'])
    def get_students():
        """Get all students"""
        try:
            session = db_session()
            students = session.query(Student).all()
            result = [student.to_dict() for student in students]
            session.close()
            return jsonify({
                'success': True,
                'data': result,
                'count': len(result)
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 500

    @api.route('/teachers', methods=['GET'])
    def get_teachers():
        """Get all teachers"""
        try:
            session = db_session()
            teachers = session.query(Teacher).all()
            result = [teacher.to_dict() for teacher in teachers]
            session.close()
            return jsonify({
                'success': True,
                'data': result,
                'count': len(result)
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 500

    @api.route('/courses', methods=['GET'])
    def get_courses():
        """Get all courses"""
        try:
            session = db_session()
            courses = session.query(Course).all()
            result = [course.to_dict() for course in courses]
            session.close()
            return jsonify({
                'success': True,
                'data': result,
                'count': len(result)
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 500

    @api.route('/enrollments', methods=['GET'])
    def get_enrollments():
        """Get all enrollment records"""
        try:
            session = db_session()
            enrollments = session.query(Enrollment).all()
            result = [enrollment.to_dict() for enrollment in enrollments]
            session.close()
            return jsonify({
                'success': True,
                'data': result,
                'count': len(result)
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 500

    @api.route('/health', methods=['GET'])
    def health_check():
        """Health check endpoint"""
        return jsonify({
            'success': True,
            'message': 'API is running'
        })

    @api.route('/register', methods=['POST'])
    def register():
        """Register a new user"""
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            
            if not username or not password or not email:
                return jsonify({
                    'success': False,
                    'message': 'Missing required fields'
                }), 400
                
            session = db_session()
            
            # Check if user exists
            existing_user = session.query(User).filter_by(username=username).first()
            if existing_user:
                session.close()
                return jsonify({
                    'success': False,
                    'message': 'Username already exists'
                }), 400
                
            new_user = User(username=username, password=password, email=email)
            session.add(new_user)
            session.commit()
            session.close()
            
            return jsonify({
                'success': True,
                'message': 'Registration successful'
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 500

    @api.route('/login', methods=['POST'])
    def login():
        """Login user"""
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            
            if not username or not password:
                return jsonify({
                    'success': False,
                    'message': 'Missing username or password'
                }), 400
                
            session = db_session()
            user = session.query(User).filter_by(username=username, password=password).first()
            session.close()
            
            if user:
                return jsonify({
                    'success': True,
                    'message': 'Login successful',
                    'data': user.to_dict()
                })
            else:
                return jsonify({
                    'success': False,
                    'message': 'Invalid username or password'
                }), 401
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 500

    app.register_blueprint(api)
