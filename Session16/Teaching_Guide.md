# Session 13 教学指南 (Teaching Guide)

本指南将指导你如何实现用户注册和登录功能。\
This guide will walk you through implementing user registration and login functionality.

## 目标 (Objectives)
1.  创建用户数据模型 (Create User Data Model)
2.  实现注册和登录 API (Implement Register and Login APIs)
3.  创建注册和登录页面 (Create Register and Login Pages)

---

## 第一步：创建用户模型 (Step 1: Create User Model)

我们需要在 `backend/models.py` 中添加 `User` 类。\
We need to add the `User` class in `backend/models.py`.

**修改文件 (File):** `backend/models.py`

**代码内容 (Content):**

```python
# 新增：
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
```

---

## 第二步：实现 API 路由 (Step 2: Implement API Routes)

我们需要在 `backend/routes.py` 中添加注册和登录的接口。\
We need to add register and login endpoints in `backend/routes.py`.

**修改文件 (File):** `backend/routes.py`

首先，添加必要的导入：
First, add necessary imports:

```python
# 新增：
from flask import request
from models import User
```

然后，添加路由函数：
Then, add route functions:

```python
    # 新增：
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

    # 新增：
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
```

---

## 第三步：前端 API 调用 (Step 3: Frontend API Calls)

我们需要在 `frontend/js/api.js` 中添加 `registerUser` 和 `loginUser` 函数。\
We need to add `registerUser` and `loginUser` functions in `frontend/js/api.js`.

**修改文件 (File):** `frontend/js/api.js`

```javascript
// 新增：
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

// 新增：
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
```

---

## 第四步：创建前端页面 (Step 4: Create Frontend Pages)

我们需要创建注册和登录页面。\
We need to create register and login pages.

**新建文件 (New File):** `frontend/register.html`
**新建文件 (New File):** `frontend/login.html`

并在 `frontend/index.html` 中添加链接。\
And add links in `frontend/index.html`.

```html
            <!-- 新增： -->
            <li><a href="register.html">Register</a></li>
            <li><a href="login.html">Login</a></li>
```
