# 📚 Student Management System

## 🚀 Overview

This is a **Python-based Student Management System** built to manage student records efficiently using **JSON file storage**.

The system allows users to **add, view, update, search, and delete student records** with structured data handling.
It follows a clean modular structure inspired by real-world backend applications.

---

## 🛠️ Features

### ✅ Core Features

* ➕ Add new student
* 📋 View all students
* 🔍 Search student by admission number
* ✏️ Update student details
* ❌ Delete student records
* 💾 Persistent storage using JSON

---

## 🧱 Data Structure

Each student record is stored as a dictionary inside a list:

```json
[
  {
    "admission_no": 1,
    "roll_no": "9-1",
    "name": "Anchal",
    "age": 15,
    "std": "9",
    "parent": {
      "father_name": "Ramadhar Yadav",
      "mother_name": "Pushpa Yadav"
    },
    "bus": {
      "location": "far",
      "fee": 1500
    }
  }
]
```

---

## 📂 Project Structure

```
student_management/
│
├── app/
│   ├── core/
│   │   └── service/
│   │       └── student_service.py
│   │
│   ├── models/
│   │   ├── student.py
│   │   └── parent.py
│   │
│   ├── storage/
│   │   └── json_storage.py
│   │
│   └── presentation/
│       └── cli/
│           └── main_cli.py
│
├── data/
│   └── students.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
```

---

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python3 main.py
```

---

## 💡 How It Works

* Data is stored in a **JSON file as a list of dictionaries**
* Each operation (Add, Update, Delete) modifies the list
* The entire list is saved back to maintain consistency
* CLI-based interaction for simplicity and learning

---

## 🧠 Concepts Used

* Python OOP (Classes & Objects)
* File Handling (JSON)
* List & Dictionary Operations
* Clean Code Structure (Separation of Concerns)

---

## 🚀 Future Improvements

* 🌐 Convert into web app (Flask / Django)
* 🗄️ Replace JSON with database (MySQL / MongoDB)
* 🔐 Add authentication system
* 📊 Add reporting & analytics

---

## 📌 Author

**Aman**
Aspiring Python Developer 🚀
Focused on Backend Development & Data Analytics

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
