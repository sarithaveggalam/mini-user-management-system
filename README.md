## 🧑‍💻 Mini User Management System

## 📌 Project Overview

The **Mini User Management System** is a full-stack web application developed to demonstrate user authentication, role-based access control, and secure API communication.
It allows users to **register, log in, and access protected resources**, while admins can manage users efficiently.

This project reflects **real-world backend and frontend development practices** using modern tools and clean architecture.

---

## 🚀 Features

### 🔐 Authentication

* User Signup
* User Login
* Password hashing for security
* JWT-based authentication

### 👥 Roles & Access

* Admin role
* Normal user role
* Role-based access control

### 📊 User Management

* View users (Admin only)
* Pagination support for large data

### 🌐 Full-Stack Application

* REST APIs (Backend)
* React UI (Frontend)
* MongoDB Atlas (Cloud Database)

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* MongoDB Atlas
* JWT Authentication
* Flask-CORS
* PyMongo

### Frontend

* React.js
* Axios
* HTML, CSS, JavaScript

### Tools

* Postman (API testing)
* GitHub (Version control)

---

## 📂 Project Structure

```
mini-user-management-system/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── package.json
│   └── src/
│       ├── App.js
│       ├── Login.js
│       ├── Signup.js
│       └── api.js
│
└── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

---

### 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs on:

```
http://localhost:3000
```

---

## 🔗 API Endpoints

### Signup API

```
POST /signup
```

```json
{
  "full_name": "User Name",
  "email": "user@example.com",
  "password": "StrongPassword"
}
```

### Login API

```
POST /login
```

```json
{
  "email": "user@example.com",
  "password": "StrongPassword"
}
```

---

## 🗄️ Database

* MongoDB Atlas (Cloud)
* Collections are created automatically
* Secure connection using environment variables

---

## 🎥 Execution Video

The execution video demonstrates:

* User signup through UI
* User login through UI
* API testing using Postman
* MongoDB data storage

---

## 📌 Learning Outcomes

* Full-stack application development
* REST API design
* JWT authentication
* MongoDB integration
* Clean project structure
* Frontend & backend integration

---

## 👩‍💻 Developed By

**Saritha Veggalam**
Backend Developer (Fresher)
