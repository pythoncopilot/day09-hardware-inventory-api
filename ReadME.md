# 📘 Day 9 — REST API Fundamentals + Backend Logging System

## 🎯 Objective
Build a REST API from scratch using Flask and SQLite, and evolve it into a monitored backend system.

---

## 🧠 Key Concepts Learned

### 1. REST API Basics
- GET / POST / PUT / DELETE
- Resource-based routing
- JSON request/response structure

### 2. Flask Web Framework
- Creating a web server in Python
- Defining API endpoints using routes
- Handling HTTP requests

### 3. SQLite Database Integration
- Creating tables programmatically
- Performing CRUD operations:
  - Create
  - Read
  - Update
  - Delete

### 4. Backend Logging System (NEW)
- Tracking every API request
- Storing logs in database
- Recording:
  - endpoint
  - HTTP method
  - success/failure status
  - timestamp

---

## 🏗️ System Architecture

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /devices | Get all devices |
| GET | /devices/{id} | Get single device |
| POST | /devices | Add device |
| PUT | /devices/{id} | Update device |
| DELETE | /devices/{id} | Delete device |

---

## 📊 Logging System

Every API request is tracked in the database:

- Endpoint used
- HTTP method
- Success or failure status
- Timestamp

This introduces **observability in backend systems**.

---

## 🔥 What Makes This Project Important

This is not just a CRUD API:

✔ REST API design  
✔ Database integration  
✔ Input validation  
✔ Error handling  
✔ Backend logging system  
✔ Production-style response structure  

---

## 🚀 Current Level

**Level: REST API + Observability Layer**

You now have a mini backend system similar to real-world APIs used in:
- IoT systems
- Cloud services
- Web applications