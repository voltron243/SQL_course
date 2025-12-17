// API Call Wrapper

// API Base URL - Modify according to your setup
const API_BASE_URL = 'http://localhost:8080/api';

/**
 * Generic API request function
 * @param {string} endpoint - API endpoint
 * @returns {Promise} - Returns data
 */
async function apiRequest(endpoint) {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`);
        
        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }
        
        const result = await response.json();
        
        if (!result.success) {
            throw new Error(result.message || 'Request failed');
        }
        
        return result.data;
    } catch (error) {
        console.error('API request failed:', error);
        throw error;
    }
}

/**
 * Fetch all students
 */
async function fetchStudents() {
    return await apiRequest('/students');
}

/**
 * Fetch all teachers
 */
async function fetchTeachers() {
    return await apiRequest('/teachers');
}

/**
 * Fetch all courses
 */
async function fetchCourses() {
    return await apiRequest('/courses');
}

/**
 * Fetch all enrollment records
 */
async function fetchEnrollments() {
    return await apiRequest('/enrollments');
}

/**
 * Register a new user
 * @param {Object} userData - {username, password, email}
 */
async function registerUser(userData) {
    try {
        const response = await fetch(`${API_BASE_URL}/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        });
        
        const result = await response.json();
        
        if (!result.success) {
            throw new Error(result.message || 'Registration failed');
        }
        
        return result;
    } catch (error) {
        console.error('Registration failed:', error);
        throw error;
    }
}

/**
 * Login user
 * @param {Object} credentials - {username, password}
 */
async function loginUser(credentials) {
    try {
        const response = await fetch(`${API_BASE_URL}/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(credentials)
        });
        
        const result = await response.json();
        
        if (!result.success) {
            throw new Error(result.message || 'Login failed');
        }
        
        return result;
    } catch (error) {
        console.error('Login failed:', error);
        throw error;
    }
}
