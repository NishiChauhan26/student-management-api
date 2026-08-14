# Student Management REST API

A RESTful API built with Flask for managing student records, featuring JWT-based authentication, input validation, and persistent JSON storage. Developed as part of the Python Development Internship at Kinetrexa Software Private Limited.

## Features

- **JWT Authentication** – Login endpoint issues a token; protected routes require it
- **Full CRUD Operations** – Create, read, update, and delete student records
- **Input Validation** – Required fields are checked before creating a record
- **Error Handling** – Proper HTTP status codes for missing tokens, invalid tokens, missing records, and bad input
- **Persistent Storage** – All data is saved to `students.json` and reloaded automatically on server restart
- **Public Read Access** – Viewing students does not require authentication; modifying data does

## Technologies Used

- Python 3
- Flask
- PyJWT (JSON Web Tokens)
- Flask-CORS
- JSON file storage

## Project Structure
student_api/
├── app.py # Main Flask application (all routes and logic)
├── students.json # Auto-generated data file
├── Student_Management_API.postman_collection.json # Postman collection for testing
└── README.md

## Setup and Installation

1. Clone this repository: 
   git clone <your-repo-url>
   cd student_api

2. Create and activate a virtual environment:
   python -m venv .venv
   .venv\Scripts\activate # Windows

3. Install dependencies:
   pip install flask pyjwt flask-cors

4. Run the application:
   python app.py

5. The API will be available at `http://127.0.0.1:5000`

## Authentication

Login credentials (demo/admin account):
Username: admin
Password: admin123

Send a `POST` request to `/login` with these credentials to receive a JWT token. Include this token in the `Authorization` header as `Bearer <token>` for all protected endpoints. Tokens expire after 1 hour.

## API Endpoints

| Method | Endpoint | Auth Required | Description |
|--------|----------|:---:|---|
| POST | `/login` | No | Authenticate and receive a JWT token |
| POST | `/students` | Yes | Create a new student record |
| GET | `/students` | No | Retrieve all student records |
| GET | `/students/<id>` | No | Retrieve a single student by ID |
| PUT | `/students/<id>` | Yes | Update an existing student record |
| DELETE | `/students/<id>` | Yes | Delete a student record |

Full request/response examples are available in `API_DOCUMENTATION.md` and the included Postman collection.

## Testing

A complete Postman collection (`Student_Management_API.postman_collection.json`) is included in this repository. Import it into Postman to test all endpoints, including the authentication flow.

## Author

Nishi Chauhan

Python Development 
