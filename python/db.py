import sqlite3
from datetime import datetime

DB_PATH = "database/inventory.db"


# =========================
# INIT DATABASE
# =========================
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Devices table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()

    # Ensure logs table exists
    init_logs_table()


# =========================
# LOGS TABLE
# =========================
def init_logs_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            endpoint TEXT,
            method TEXT,
            status TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


# =========================
# ADD DEVICE
# =========================
def add_device(name, status):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO devices (name, status, created_at)
        VALUES (?, ?, ?)
    """, (
        name,
        status,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


# =========================
# GET ALL DEVICES
# =========================
def get_devices():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM devices")
    rows = cursor.fetchall()

    conn.close()
    return rows


# =========================
# GET SINGLE DEVICE
# =========================
def get_device(device_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM devices WHERE id=?", (device_id,))
    row = cursor.fetchone()

    conn.close()
    return row


# =========================
# UPDATE DEVICE
# =========================
def update_device(device_id, status):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE devices
        SET status=?
        WHERE id=?
    """, (status, device_id))

    conn.commit()
    conn.close()


# =========================
# DELETE DEVICE
# =========================
def delete_device(device_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM devices WHERE id=?", (device_id,))

    conn.commit()
    conn.close()


# =========================
# ADD LOG ENTRY
# =========================
def add_log(endpoint, method, status):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO logs (endpoint, method, status, timestamp)
        VALUES (?, ?, ?, ?)
    """, (
        endpoint,
        method,
        status,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()