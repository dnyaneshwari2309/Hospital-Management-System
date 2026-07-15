# 🏥 Hospital Management System
A Python + MySQL CLI application to digitize and manage patient records for healthcare staff.

## 💡 Why I Built This
I was talking to someone who works at a small clinic, and found out they were still managing patient records in physical registers. Searching for a patient meant flipping through pages. Updating records was even messier. It was exactly the kind of problem a simple database-backed application could fix.

So I built one over a weekend.

This project helped me solidify database design, normalized schemas, and safe SQL practices — things I had studied but wanted to apply on a real use case.

## 🚀 Features
✅ Full CRUD — patients, doctors, appointments, medical history
✅ Normalized MySQL schema (3NF) — eliminates data redundancy
✅ Parameterized SQL queries — prevents SQL injection
✅ Structured CLI — clean menus, no GUI overhead
✅ Modular codebase — each feature in its own file, easy to extend
✅ Environment-based config — credentials never hardcoded
## 🗂️ Project Structure
hospital_management_system/
│
├── main.py                      # CLI entry point
│
├── database/
│   ├── db_connection.py         # MySQL connection (env-based)
│   └── schema.sql               # Full DB schema + seed data
│
├── modules/
│   ├── patient.py               # Patient CRUD
│   ├── doctor.py                # Doctor management
│   ├── appointment.py           # Appointment scheduling
│   └── medical_history.py       # Medical records
│
├── utils/
│   └── helpers.py               # CLI display utilities
│
├── .env.example                 # Credential template
├── requirements.txt
└── .gitignore
# 🛠️ Tech Stack
Layer	Technology
Language	Python 3.10+
Database	MySQL 8.x
Connector	mysql-connector-python
Interface	CLI
Config	python-dotenv
## ⚙️ Setup & Run
### 1. Clone the repo
git clone https://github.com/dnyaneshwari2309/hospital-management-system.git
cd hospital-management-system
### 2. Install dependencies
pip install -r requirements.txt
### 3. Set up the database
mysql -u root -p < database/schema.sql
### 4. Configure credentials
cp .env.example .env
Edit .env with your MySQL password.
### 5. Run
python main.py
## 📸 CLI Preview
╔══════════════════════════════════════════════════════════╗
║           HOSPITAL MANAGEMENT SYSTEM                     ║
║           Developed by Dnyaneshwari Sonawane                   ║
║           DYPCOEI, SPPU, Pune                              ║
╚══════════════════════════════════════════════════════════╝

  MAIN MENU
  ---------
  1. Patient Management
  2. Doctor Management
  3. Appointment Management
  4. Medical History
  0. Exit
## 🗃️ Database Schema (3NF)
patients        → patient_id, name, dob, gender, blood_group, phone, email, address
doctors         → doctor_id, name, specialization, phone, email, available
appointments    → appointment_id, patient_id*, doctor_id*, date, time, reason, status
medical_history → history_id, patient_id*, doctor_id*, diagnosis, prescription, visit_date, notes
Foreign keys use ON DELETE CASCADE to keep data consistent and avoid orphaned records.

## 🔐 Security
Every query uses parameterized statements (%s placeholders). User input is never concatenated directly into SQL — a simple but critical practice often skipped in beginner projects.

## 📌 What I Learned
Designing a schema in Third Normal Form (3NF)
Why parameterized queries matter beyond just theory
Structuring Python projects into proper packages
Using .env files to keep credentials out of source code
## 🔮 Future Plans
 Billing and invoicing module
 Export patient reports as PDF
 Role-based login (admin / doctor / receptionist)
 Flask web interface
## 👨‍💻 Author
Dnyaneshwari Sonawane B.E — Artificial Intelligence and Data Science DYPCOEI, SPPU, Pune
