from flask import Blueprint, jsonify
from models import Course, Enrollment, Student, Teacher

# Flask in a class
api = Blueprint('api', __name__, url_prefix='/api')


# Pass the value into the API 
def init_routes(app, db_session):
    
    """"
    Student 
    Teacher
    Course 
    Enrollment
    """
   
   # Decoration - Not changing the original function code
   # Students
    @api.route('/students', methods=['GET'])
    def get_students():
        try:
            session = db_session()
            #ORM - Student model will fetch the data to the database
            # Just like SELECT * FROM `Student`
            students = session.query(Student).all()
            # Front end can recieve the JSON file, we need a dictionary for it
            result = [student.to_dict() for student in students] # List is the best option and dictionary
            # We need to close the session
            session.close()
            # front end can only accept the json file
            # Changing the dictionary file into a json file
            return jsonify(
                {
                    'success': True,
                    'data': result,
                    'count': len(result)
                }      
            )
        # If there is an error
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)  
            }), 500 # Error is actually caused by the status of the backend
    
    # Teachers  
    @api.route('/teachers', methods=['GET'])
    def get_teachers():
        try:
            session = db_session()
            teachers = session.query(Teacher).all()
            result = [teacher.to_dict() for teacher in teachers]
            session.close()
            return jsonify(
                 {
                    'success': True,
                    'data': result,
                    'count': len(result)
                } 
            )   
        # If there is an error
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)  
            }), 500 
            
    # Courses  
    @api.route('/courses', methods=['GET'])
    def get_courses():
        try:
            session = db_session()
            courses = session.query(Course).all()
            result = [course.to_dict() for course in courses]
            session.close()
            return jsonify(
                 {
                    'success': True,
                    'data': result,
                    'count': len(result)
                } 
            )   
        # If there is an error
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)  
            }), 500 
    
    # Enrollment 
    @api.route('/enrollments', methods=['GET'])          
    def get_enrollments():
        try:
            session = db_session()
            enrollments = session.query(Enrollment).all()
            result = [enrollment.to_dict() for enrollment in enrollments]
            session.close()
            return jsonify(
                {
                    'success': True,
                    'data': result,
                    'count': len(result)
                } 
            )   
        # If there is an error
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)  
            }), 500 
            
    @api.route('/health', methods=['GET'])
    def health_check():
        return jsonify(
            {
                'success': True,
                'message': 'API is running'
            }
        )
    
    app.register_blueprint(api)        
        
            
            
            
            
            