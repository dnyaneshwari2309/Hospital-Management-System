"""
medical_history.py
------------------
Author  : Dnyaneshwari Sonawane 
College : DYPCOEI, SPPU, Pune

Log and retrieve patient medical records.
"""

from database.db_connection import get_connection


def add_medical_record():
    print("\n--- Add Medical Record ---")
    pid          = input("Patient ID            : ").strip()
    did          = input("Doctor ID             : ").strip()
    diagnosis    = input("Diagnosis             : ").strip()
    prescription = input("Prescription          : ").strip()
    visit_date   = input("Visit Date (YYYY-MM-DD): ").strip()
    notes        = input("Notes (optional)      : ").strip() or None
    conn         = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO medical_history (patient_id, doctor_id, diagnosis, prescription, visit_date, notes)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (pid, did, diagnosis, prescription, visit_date, notes),
        )
        conn.commit()
        print(f"\n  ✔ Medical record added (ID: {cur.lastrowid}).")
    except Exception as e:
        print(f"\n  ✖ Error: {e}")
    finally:
        conn.close()


def view_medical_history():
    pid  = input("\nPatient ID: ").strip()
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            """SELECT mh.history_id, p.name, d.name, mh.diagnosis,
                      mh.prescription, mh.visit_date, mh.notes
               FROM medical_history mh
               JOIN patients p ON mh.patient_id = p.patient_id
               JOIN doctors  d ON mh.doctor_id  = d.doctor_id
               WHERE mh.patient_id = %s
               ORDER BY mh.visit_date DESC""",
            (pid,),
        )
        rows = cur.fetchall()
        if not rows:
            print("\n  No records found for this patient.")
            return
        for r in rows:
            print(f"\n  History ID   : {r[0]}")
            print(f"  Patient      : {r[1]}")
            print(f"  Doctor       : {r[2]}")
            print(f"  Diagnosis    : {r[3]}")
            print(f"  Prescription : {r[4]}")
            print(f"  Visit Date   : {r[5]}")
            print(f"  Notes        : {r[6] or 'N/A'}")
            print("  " + "-" * 45)
    finally:
        conn.close()
