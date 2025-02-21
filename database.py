import sqlite3
from datetime import datetime

DATABASE_NAME = "job_applications.db"


def create_connection():
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_table():
    """Create the job_applications table if it doesn't exist."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS job_applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL,
            job_title TEXT NOT NULL,
            date_applied DATE NOT NULL,
            follow_up_date DATE,
            status TEXT NOT NULL,
            notes TEXT
        )
        """
    )
    conn.commit()
    conn.close()


# Ensure the table is created when the module is imported
create_table()


def add_job_application(
    company_name, job_title, date_applied, follow_up_date, status, notes
):
    """Add a new job application to the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO job_applications (company_name, job_title, date_applied, follow_up_date, status, notes)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (company_name, job_title, date_applied, follow_up_date, status, notes),
    )
    conn.commit()
    conn.close()


def get_all_job_applications():
    """Retrieve all job applications from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM job_applications")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_job_status(job_id, new_status):
    """Update the status of a job application."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE job_applications
        SET status = ?
        WHERE id = ?
        """,
        (new_status, job_id),
    )
    conn.commit()
    conn.close()


def delete_job_application(job_id):
    """Delete a job application by ID."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM job_applications WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()


def get_upcoming_follow_ups(days):
    """Retrieve job applications with follow-up dates within the next X days."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM job_applications
        WHERE follow_up_date BETWEEN DATE('now') AND DATE('now', ?)
        """,
        (f"+{days} days",),
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
