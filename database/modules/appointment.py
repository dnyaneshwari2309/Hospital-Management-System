"""
appointment.py
--------------
Author  : Dnyaneshwari Sonawane 
College : DYPCOEI, SPPU, Pune

Schedule, view, update, and cancel appointments.
"""

from database.db_connection import get_connection


def _print_appointments(rows):
    if not rows:
        print("\n  No appointments found.")
        return
    header = f"\n{'AptID':<7} {'Patient':<20} {'Doctor':<20} {'Date':<12} {'Time':<8} {'Status'}"
    print(header)
    print("-" * 80)
    for r in rows:
        print(f"{r[0]:<7} {r[1]:<20} {r[2]:<20} {str(r[3]):<12} {str(r[4]):<8} {r[5]}")


def schedule_appointment():
    print("\n--- Schedule Appointment ---")
    pid    = input("Patient ID        : ").strip()
    did    = input("Doctor ID         : ").strip()
    date   = input("Date (YYYY-MM-DD) : ").strip()
    time   = input("Time (HH:MM)      : ").strip()
    reason = input("Reason            : ").strip()
    conn   = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, reason)
               VALUES (%s, %s, %s, %s, %s)""",
            (pid, did, date, time, reason),
        )
        conn.commit()
        print(f"\n  ✔ Appointment scheduled (ID: {cur.lastrowid}).")
    except Exception as e:
        print(f"\n  ✖ Error: {e}")
    finally:
        conn.close()


def view_all_appointments():
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            """SELECT a.appointment_id, p.name, d.name,
                      a.appointment_date, a.appointment_time, a.status
               FROM appointments a
               JOIN patients p ON a.patient_id = p.patient_id
               JOIN doctors  d ON a.doctor_id  = d.doctor_id
               ORDER BY a.appointment_date, a.appointment_time"""
        )
        _print_appointments(cur.fetchall())
    finally:
        conn.close()


def view_appointments_by_patient():
    pid  = input("\nPatient ID: ").strip()
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            """SELECT a.appointment_id, p.name, d.name,
                      a.appointment_date, a.appointment_time, a.status
               FROM appointments a
               JOIN patients p ON a.patient_id = p.patient_id
               JOIN doctors  d ON a.doctor_id  = d.doctor_id
               WHERE a.patient_id = %s
               ORDER BY a.appointment_date""",
            (pid,),
        )
        _print_appointments(cur.fetchall())
    finally:
        conn.close()


def update_appointment_status():
    print("\n--- Update Appointment Status ---")
    aid    = input("Appointment ID: ").strip()
    print("  1. Scheduled\n  2. Completed\n  3. Cancelled")
    choice = input("New Status    : ").strip()
    status_map = {"1": "Scheduled", "2": "Completed", "3": "Cancelled"}
    status = status_map.get(choice)
    if not status:
        print("  Invalid choice.")
        return
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute("UPDATE appointments SET status = %s WHERE appointment_id = %s", (status, aid))
        conn.commit()
        print(f"\n  ✔ Appointment ID {aid} marked as '{status}'.")
    except Exception as e:
        print(f"\n  ✖ Error: {e}")
    finally:
        conn.close()


def cancel_appointment():
    aid     = input("\nAppointment ID to cancel: ").strip()
    confirm = input("  Confirm cancel? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("  Cancelled.")
        return
    conn = get_connection()
    if not conn:
        return
    try:
        cur = conn.cursor()
        cur.execute("UPDATE appointments SET status = 'Cancelled' WHERE appointment_id = %s", (aid,))
        conn.commit()
        print(f"\n  ✔ Appointment ID {aid} cancelled.")
    except Exception as e:
        print(f"\n  ✖ Error: {e}")
    finally:
        conn.close()
