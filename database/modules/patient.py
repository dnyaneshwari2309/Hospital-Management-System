"""
patient.py
----------
Author  : Dnyaneshwari Sonawane 
College : DYPCOEI, SPPU, Pune

Full CRUD operations for patient records.
Parameterized queries used throughout — no raw string formatting
with user input anywhere in this file.
"""

from database.db_connection import get_connection


def _print_patients(rows):
    if not rows:
        print("\n  No patient records found.")
        return
    header = f"\n{'ID':<6} {'Name':<22} {'DOB':<12} {'Gender':<8} {'Blood':<6} {'Phone':<14} {'Email'}"
    print(header)
    print("-" * 80)
    for r in rows:
        print(f"{r[0]:<6} {r[1]:<22} {str(r[2]):<12} {r[3]:<8} {str(r[4]):<6} {r[5]:<14} {r[6] or ''}")


def add_patient():
    print("\n--- Add New Patient ---")
    name        = input("Full Name              : ").strip()
    dob         = input("Date of Birth (YYYY-MM-DD): ").strip()
    gender      = input("Gender (Male/Female/Other): ").strip()
    blood_group = input("Blood Group            : ").strip()
    phone       = input("Phone                  : ").strip()
    email       = input("Email (optional)       : ").strip() or None
    address     = input("Address                : ").strip()

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO patients (name, dob, gender, blood_group, phone, email, address)
               VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (name, dob, gender, blood_group, phone, email, address),
        )
        conn.commit()
        print(f"\n  ✔ Patient '{name}' added successfully (ID: {cur.lastrowid}).")
    except Exception as e:
        print(f"\n  ✖ Error adding patient: {e}")
    finally:
        conn.close()


def view_all_patients():
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT patient_id, name, dob, gender, blood_group, phone, email FROM patients ORDER BY patient_id"
        )
        _print_patients(cur.fetchall())
    finally:
        conn.close()


def search_patient():
    print("\n--- Search Patient ---")
    keyword = input("Enter name or phone: ").strip()
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            """SELECT patient_id, name, dob, gender, blood_group, phone, email
               FROM patients WHERE name LIKE %s OR phone LIKE %s""",
            (f"%{keyword}%", f"%{keyword}%"),
        )
        _print_patients(cur.fetchall())
    finally:
        conn.close()


def view_patient_by_id():
    pid = input("\nEnter Patient ID: ").strip()
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT patient_id, name, dob, gender, blood_group, phone, email FROM patients WHERE patient_id = %s",
            (pid,),
        )
        _print_patients(cur.fetchall())
    finally:
        conn.close()


def update_patient():
    print("\n--- Update Patient Record ---")
    pid = input("Patient ID to update: ").strip()
    print("  1. Phone\n  2. Email\n  3. Address\n  4. Blood Group")
    choice = input("Choice: ").strip()
    field_map = {
        "1": ("phone", "New Phone"),
        "2": ("email", "New Email"),
        "3": ("address", "New Address"),
        "4": ("blood_group", "New Blood Group"),
    }
    if choice not in field_map:
        print("  Invalid choice.")
        return
    col, label = field_map[choice]
    value = input(f"{label}: ").strip()

    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(f"UPDATE patients SET {col} = %s WHERE patient_id = %s", (value, pid))
        conn.commit()
        if cur.rowcount:
            print(f"\n  ✔ Patient ID {pid} updated successfully.")
        else:
            print(f"\n  ✖ No patient found with ID {pid}.")
    except Exception as e:
        print(f"\n  ✖ Update failed: {e}")
    finally:
        conn.close()


def delete_patient():
    print("\n--- Delete Patient Record ---")
    pid     = input("Patient ID to delete: ").strip()
    confirm = input(f"  Confirm delete patient ID {pid}? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("  Deletion cancelled.")
        return
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM patients WHERE patient_id = %s", (pid,))
        conn.commit()
        if cur.rowcount:
            print(f"\n  ✔ Patient ID {pid} deleted.")
        else:
            print(f"\n  ✖ No patient found with ID {pid}.")
    except Exception as e:
        print(f"\n  ✖ Deletion failed: {e}")
    finally:
        conn.close()
