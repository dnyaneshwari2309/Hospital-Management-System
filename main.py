"""
main.py
-------
Author  : Dnyaneshwari Sonawane
College : DYPCOEI, SPPU, Pune
GitHub  : https://github.com/dnyaneshwari2309

Entry point for the Hospital Management System CLI.
Run: python main.py
"""

from utils.helpers import print_banner, print_divider

from modules.patient import (
    add_patient, view_all_patients, search_patient,
    view_patient_by_id, update_patient, delete_patient,
)
from modules.doctor import (
    add_doctor, view_all_doctors, search_doctor, toggle_doctor_availability,
)
from modules.appointment import (
    schedule_appointment, view_all_appointments,
    view_appointments_by_patient, update_appointment_status, cancel_appointment,
)
from modules.medical_history import add_medical_record, view_medical_history


def patient_menu():
    while True:
        print("""
  PATIENT MANAGEMENT
  ------------------
  1. Add New Patient
  2. View All Patients
  3. Search Patient
  4. View Patient by ID
  5. Update Patient Info
  6. Delete Patient
  0. Back
""")
        c = input("  Choice: ").strip()
        if   c == "1": add_patient()
        elif c == "2": view_all_patients()
        elif c == "3": search_patient()
        elif c == "4": view_patient_by_id()
        elif c == "5": update_patient()
        elif c == "6": delete_patient()
        elif c == "0": break
        else: print("  Invalid option.")


def doctor_menu():
    while True:
        print("""
  DOCTOR MANAGEMENT
  -----------------
  1. Add New Doctor
  2. View All Doctors
  3. Search Doctor
  4. Toggle Availability
  0. Back
""")
        c = input("  Choice: ").strip()
        if   c == "1": add_doctor()
        elif c == "2": view_all_doctors()
        elif c == "3": search_doctor()
        elif c == "4": toggle_doctor_availability()
        elif c == "0": break
        else: print("  Invalid option.")


def appointment_menu():
    while True:
        print("""
  APPOINTMENT MANAGEMENT
  ----------------------
  1. Schedule Appointment
  2. View All Appointments
  3. View by Patient
  4. Update Status
  5. Cancel Appointment
  0. Back
""")
        c = input("  Choice: ").strip()
        if   c == "1": schedule_appointment()
        elif c == "2": view_all_appointments()
        elif c == "3": view_appointments_by_patient()
        elif c == "4": update_appointment_status()
        elif c == "5": cancel_appointment()
        elif c == "0": break
        else: print("  Invalid option.")


def medical_menu():
    while True:
        print("""
  MEDICAL HISTORY
  ---------------
  1. Add Medical Record
  2. View Patient History
  0. Back
""")
        c = input("  Choice: ").strip()
        if   c == "1": add_medical_record()
        elif c == "2": view_medical_history()
        elif c == "0": break
        else: print("  Invalid option.")


def main():
    print_banner()
    while True:
        print_divider()
        print("""  MAIN MENU
  ---------
  1. Patient Management
  2. Doctor Management
  3. Appointment Management
  4. Medical History
  0. Exit
""")
        c = input("  Choice: ").strip()
        if   c == "1": patient_menu()
        elif c == "2": doctor_menu()
        elif c == "3": appointment_menu()
        elif c == "4": medical_menu()
        elif c == "0":
            print("\n  Goodbye! — Omkar Avasarkar\n")
            break
        else:
            print("  Invalid option. Try again.")


if __name__ == "__main__":
    main()
