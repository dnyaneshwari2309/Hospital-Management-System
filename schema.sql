-- ============================================================
-- Hospital Management System - Database Schema
-- Author : Omkar Avasarkar
-- College : SRCOE, SPPU, Pune
-- Description : Normalized relational schema (3NF) covering
--               patients, doctors, appointments, medical history
-- ============================================================

CREATE DATABASE IF NOT EXISTS hospital_db;
USE hospital_db;

-- -----------------------------------------------
-- Table: doctors
-- -----------------------------------------------
CREATE TABLE IF NOT EXISTS doctors (
    doctor_id      INT AUTO_INCREMENT PRIMARY KEY,
    name           VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    phone          VARCHAR(15)  UNIQUE NOT NULL,
    email          VARCHAR(100) UNIQUE NOT NULL,
    available      BOOLEAN DEFAULT TRUE,
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------
-- Table: patients
-- -----------------------------------------------
CREATE TABLE IF NOT EXISTS patients (
    patient_id  INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    dob         DATE NOT NULL,
    gender      ENUM('Male', 'Female', 'Other') NOT NULL,
    blood_group VARCHAR(5),
    phone       VARCHAR(15) UNIQUE NOT NULL,
    email       VARCHAR(100),
    address     TEXT,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------
-- Table: appointments
-- -----------------------------------------------
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id   INT AUTO_INCREMENT PRIMARY KEY,
    patient_id       INT NOT NULL,
    doctor_id        INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    reason           VARCHAR(255),
    status           ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id)  REFERENCES doctors(doctor_id)   ON DELETE CASCADE
);

-- -----------------------------------------------
-- Table: medical_history
-- -----------------------------------------------
CREATE TABLE IF NOT EXISTS medical_history (
    history_id   INT AUTO_INCREMENT PRIMARY KEY,
    patient_id   INT NOT NULL,
    doctor_id    INT NOT NULL,
    diagnosis    TEXT NOT NULL,
    prescription TEXT,
    visit_date   DATE NOT NULL,
    notes        TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id)  REFERENCES doctors(doctor_id)   ON DELETE SET NULL
);

-- -----------------------------------------------
-- Sample seed data
-- -----------------------------------------------
INSERT INTO doctors (name, specialization, phone, email) VALUES
('Dr. Rajesh Sharma', 'Cardiologist', '9876543210', 'rajesh@hospital.com'),
('Dr. Priya Mehta',   'Neurologist',  '9876543211', 'priya@hospital.com'),
('Dr. Amit Desai',    'Orthopedic',   '9876543212', 'amit@hospital.com');

INSERT INTO patients (name, dob, gender, blood_group, phone, email, address) VALUES
('Rahul Patil',  '1990-05-14', 'Male',   'B+', '9000000001', 'rahul@mail.com',  'Pune, MH'),
('Sneha Joshi',  '1995-08-22', 'Female', 'O+', '9000000002', 'sneha@mail.com',  'Mumbai, MH'),
('Vikram Singh', '1985-01-30', 'Male',   'A-', '9000000003', 'vikram@mail.com', 'Nagpur, MH');
