# 📚 Study Tracker API (Django REST Framework)

## 🔹 Project Overview

The **Study Tracker API** is a RESTful backend application built using **Django** and **Django REST Framework (DRF)**. It allows users to record and track their daily study activities.

Users can:

* Log subjects studied
* Record hours spent studying
* Track study dates
* Monitor productivity and consistency over time

This project demonstrates:

* CRUD operations
* User authentication
* Data filtering
* Aggregation (total hours per subject)

---

## 🚀 Features

### 🔐 Authentication

* User registration
* User login (JWT or Session Authentication)
* User-specific study records

### 📖 Study Management

* Add daily study entries
* View study history
* Update study records
* Delete study entries
* Filter by subject
* Filter by date
* View total hours studied per subject

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (default) or PostgreSQL

---

## 📂 Project Structure

```
study_tracker/
│
├── users/              # User authentication logic
├── study/              # Study entry app
├── study_tracker/      # Project settings
└── manage.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/study-tracker-api.git
cd study-tracker-api
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the server

```bash
python manage.py runserver
```

API will be available at:

```
http://127.0.0.1:8000/api/
```

---

## 🎯 Learning Objectives

This project demonstrates:

* REST API design
* Authentication and authorization
* Query parameter filtering
* Aggregation using Django ORM
* Clean project structure

---

## 📌 Future Improvements

* Add weekly/monthly analytics
* Add pagination
* Add rate limiting
* Add study goals feature
* Deploy to cloud (Render, Railway, or Heroku alternative)
