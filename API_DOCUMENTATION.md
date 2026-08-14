# API Documentation — Student Management System

Base URL: `http://127.0.0.1:5000`

All request and response bodies are in JSON format.

---

## 1. Login

Authenticate and receive a JWT token.

**Endpoint:** `POST /login`
**Authentication:** Not required

**Request Body:**
```json
{
    "username": "admin",
    "password": "admin123"
}
```

**Success Response — 200 OK**
```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Error Response — 401 Unauthorized**
```json
{
    "error": "Invalid username or password"
}
```

---

## 2. Add Student

Create a new student record.

**Endpoint:** `POST /students`
**Authentication:** Required (Bearer Token)

**Headers:**
```
Authorization: Bearer <your_token_here>
Content-Type: application/json
```

**Request Body:**
```json
{
    "name": "Nishi Chauhan",
    "age": 20,
    "course": "Python Development",
    "marks": 92
}
```
*Required fields: `name`, `course`. Optional: `age`, `marks`.*

**Success Response — 201 Created**
```json
{
    "id": 1,
    "name": "Nishi Chauhan",
    "age": 20,
    "course": "Python Development",
    "marks": 92
}
```

**Error Response — 400 Bad Request** (missing required field)
```json
{
    "error": "name and course are required"
}
```

**Error Response — 401 Unauthorized** (no/invalid token)
```json
{
    "error": "Token is missing"
}
```

---

## 3. View All Students

Retrieve every student record.

**Endpoint:** `GET /students`
**Authentication:** Not required

**Success Response — 200 OK**
```json
[
    {
        "id": 1,
        "name": "Nishi Chauhan",
        "age": 20,
        "course": "Python Development",
        "marks": 92
    }
]
```

---

## 4. Get Student by ID

Retrieve a single student record.

**Endpoint:** `GET /students/<id>`
**Authentication:** Not required

**Success Response — 200 OK**
```json
{
    "id": 1,
    "name": "Nishi Chauhan",
    "age": 20,
    "course": "Python Development",
    "marks": 92
}
```

**Error Response — 404 Not Found**
```json
{
    "error": "Student not found"
}
```

---

## 5. Update Student

Update an existing student's details. Only fields included in the request body are changed; all others are left as-is.

**Endpoint:** `PUT /students/<id>`
**Authentication:** Required (Bearer Token)

**Request Body (example — partial update):**
```json
{
    "marks": 98
}
```

**Success Response — 200 OK**
```json
{
    "id": 1,
    "name": "Nishi Chauhan",
    "age": 20,
    "course": "Python Development",
    "marks": 98
}
```

**Error Response — 404 Not Found**
```json
{
    "error": "Student not found"
}
```

---

## 6. Delete Student

Remove a student record permanently.

**Endpoint:** `DELETE /students/<id>`
**Authentication:** Required (Bearer Token)

**Success Response — 200 OK**
```json
{
    "message": "Student 1 deleted"
}
```

**Error Response — 404 Not Found**
```json
{
    "error": "Student not found"
}
```

---

## Status Code Summary

| Code | Meaning |
|------|---------|
| 200 | Request succeeded |
| 201 | Resource created successfully |
| 400 | Bad request (missing/invalid input) |
| 401 | Unauthorized (missing, invalid, or expired token; or wrong login credentials) |
| 404 | Resource not found |