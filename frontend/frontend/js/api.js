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

// Homework: Implement fetchCourses and fetchEnrollments
