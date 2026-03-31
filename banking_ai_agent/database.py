import sqlite3

def get_connection():
    return sqlite3.connect("support_tickets.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS support_tickets (
        ticket_id TEXT PRIMARY KEY,
        customer_name TEXT,
        issue TEXT,
        status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def insert_ticket(ticket_id, customer_name, issue, status="Unresolved"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO support_tickets (ticket_id, customer_name, issue, status)
    VALUES (?, ?, ?, ?)
    """, (ticket_id, customer_name, issue, status))

    conn.commit()
    conn.close()

def get_ticket_status(ticket_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT status FROM support_tickets WHERE ticket_id = ?
    """, (ticket_id,))

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    return None
