"""
doctor.py
---------
Author  : Dnyaneshwari Sonawane 
College : DYPCOEI, SPPU, Pune

CRUD operations for doctor records.
"""

from database.db_connection import get_connection


def _print_doctors(rows):
    if not rows:
        print("\n  No doctor records found.")
        return
    header = f"\n{'ID':<6} {'Name':<25} {'Specialization':<20} {'Phone':<14} {'Available'}"
    print(header)
    print("-" * 75)
    for r in rows:
        avail = "Yes" if r[4] else "No"
        print(f"{r[0]:<6} {r[1]:<25} {r[2]:<20} {r[3]:<14} {avail}")


def add_doctor():
    print("\n--- Add New Doctor ---")
    name  = input("Full Name         : ").strip()
    spec  = input("Specialization    : ").strip()
    phone = input("Phone             : ").strip()
    email = input("Email             : ").strip()
    conn  = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO doctors (name, specialization, phone, email) VALUES (%s, %s, %s, %s)",
            (name, spec, phone, email),
        )
        conn.commit()
        print(f"\n  ✔ Dr. {name} added (ID: {cur.lastrowid}).")
    except Exception as e:
        print(f"\n  ✖ Error: {e}")
    finally:
        conn.close()


def view_all_doctors():
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT doctor_id, name, specialization, phone, available FROM doctors ORDER BY doctor_id"
        )
        _print_doctors(cur.fetchall())
    finally:
        conn.close()


def search_doctor():
    keyword = input("\nEnter name or specialization: ").strip()
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            """SELECT doctor_id, name, specialization, phone, available
               FROM doctors WHERE name LIKE %s OR specialization LIKE %s""",
            (f"%{keyword}%", f"%{keyword}%"),
        )
        _print_doctors(cur.fetchall())
    finally:
        conn.close()


def toggle_doctor_availability():
    did  = input("\nDoctor ID: ").strip()
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute("UPDATE doctors SET available = NOT available WHERE doctor_id = %s", (did,))
        conn.commit()
        print(f"\n  ✔ Availability toggled for Doctor ID {did}.")
    except Exception as e:
        print(f"\n  ✖ Error: {e}")
    finally:
        conn.close()
