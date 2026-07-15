# 🏥 Hospital Management System

A Python + MySQL CLI application to digitize and manage patient records for healthcare staff.

---

## 💡 Why I Built This

I was talking to someone who works at a small clinic and found out they were still managing patient records in physical registers. Searching for a patient meant flipping through pages. Updating records was even messier. It was exactly the kind of problem a simple database-backed application could fix.

So I built one over a weekend.

This project helped me solidify database design, normalized schemas, and safe SQL practices—things I had studied but wanted to apply to a real-world use case.

---

## 🚀 Features

- ✅ Full CRUD operations for patients, doctors, appointments, and medical history
- ✅ Normalized MySQL schema (3NF) to eliminate data redundancy
- ✅ Parameterized SQL queries to prevent SQL injection
- ✅ Structured CLI with clean navigation menus
- ✅ Modular codebase for easy maintenance and scalability
- ✅ Environment-based configuration using `.env`

---

## 🛠️ Tech Stack

| Layer | Technology |
|---------|------------|
| Language | Python 3.10+ |
| Database | MySQL 8.x |
| Connector | mysql-connector-python |
| Interface | Command Line Interface (CLI) |
| Configuration | python-dotenv |

---

## 🗂️ Project Structure

```text
hospital_management_system/
│
├── main.py
│
├── database/
│   ├── db_connection.py
│   └── schema.sql
│
├── modules/
│   ├── patient.py
│   ├── doctor.py
│   ├── appointment.py
│   └── medical_history.py
│
├── utils/
│   └── helpers.py
│
├── .env.example
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Setup & Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dnyaneshwari2309/hospital-management-system.git
cd hospital-management-system
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up the Database

```bash
mysql -u root -p < database/schema.sql
```

### 4️⃣ Configure Environment Variables

```bash
cp .env.example .env
```

Update the `.env` file with your MySQL credentials.

### 5️⃣ Run the Application

```bash
python main.py
```

---

## 📸 CLI Preview

```text
╔══════════════════════════════════════════════════════════╗
║           HOSPITAL MANAGEMENT SYSTEM                     ║
║           Developed by Dnyaneshwari Sonawane             ║
║           DYPCOEI, SPPU, Pune                            ║
╚══════════════════════════════════════════════════════════╝

  MAIN MENU
  ---------
  1. Patient Management
  2. Doctor Management
  3. Appointment Management
  4. Medical History
  0. Exit
```

---

## 🗃️ Database Schema (3NF)

| Table | Fields |
|---------|---------|
| Patients | patient_id, name, dob, gender, blood_group, phone, email, address |
| Doctors | doctor_id, name, specialization, phone, email, available |
| Appointments | appointment_id, patient_id, doctor_id, date, time, reason, status |
| Medical History | history_id, patient_id, doctor_id, diagnosis, prescription, visit_date, notes |

Foreign keys use **ON DELETE CASCADE** to maintain referential integrity and prevent orphaned records.

---

## 🔐 Security

Every database query uses parameterized statements (`%s` placeholders). User input is never concatenated directly into SQL queries, reducing the risk of SQL injection attacks.

---

## 📌 What I Learned

- Database normalization and Third Normal Form (3NF)
- Importance of parameterized SQL queries
- Structuring Python projects into modular packages
- Using environment variables for secure configuration management
- Building scalable CRUD applications with MySQL

---

## 🔮 Future Enhancements

- 📄 Billing and invoicing module
- 📊 Export patient reports as PDF
- 👤 Role-based authentication (Admin / Doctor / Receptionist)
- 🌐 Flask web interface
- 📱 Responsive web dashboard

---

## 👨‍💻 Author

**Dnyaneshwari Sonawane**  
B.E. Artificial Intelligence & Data Science  
DYPCOEI, SPPU, Pune

---

## 🌐 Connect With Me

[![GitHub](https://img.shields.io/badge/GitHub-dnyaneshwari2309-black?logo=github)](https://github.com/dnyaneshwari2309)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Dnyaneshwari%20Sonawane-blue?logo=linkedin)](https://www.linkedin.com/in/dnyaneshwari-sonawane-7b8a04243/))
