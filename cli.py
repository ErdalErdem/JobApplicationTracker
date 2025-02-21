import argparse
from database import (
    add_job_application,
    get_all_job_applications,
    update_job_status,
    delete_job_application,
    get_upcoming_follow_ups,
)


def display_menu():
    """Display the CLI menu."""
    print("\nJob Application Tracker")
    print("1. Add Job Application")
    print("2. View All Job Applications")
    print("3. Update Job Status")
    print("4. Delete Job Application")
    print("5. View Upcoming Follow-ups")
    print("6. Exit")


def add_job():
    """Add a new job application."""
    company_name = input("Enter company name: ")
    job_title = input("Enter job title: ")
    date_applied = input("Enter date applied (YYYY-MM-DD): ")
    follow_up_date = input("Enter follow-up date (YYYY-MM-DD): ")
    status = input("Enter status (Applied, Interview, Offer, Rejected, etc.): ")
    notes = input("Enter notes: ")
    add_job_application(
        company_name, job_title, date_applied, follow_up_date, status, notes
    )
    print("Job application added successfully!")


def view_all_jobs():
    """View all job applications."""
    jobs = get_all_job_applications()
    for job in jobs:
        print(
            f"\nID: {job[0]}, Company: {job[1]}, Title: {job[2]}, Applied: {job[3]}, Follow-up: {job[4]}, Status: {job[5]}, Notes: {job[6]}"
        )


def update_status():
    """Update the status of a job application."""
    job_id = input("Enter job ID to update: ")
    new_status = input("Enter new status: ")
    update_job_status(job_id, new_status)
    print("Job status updated successfully!")


def delete_job():
    """Delete a job application."""
    job_id = input("Enter job ID to delete: ")
    delete_job_application(job_id)
    print("Job application deleted successfully!")


def view_upcoming_follow_ups():
    """View upcoming follow-ups."""
    days = input("Enter number of days to check for follow-ups: ")
    follow_ups = get_upcoming_follow_ups(days)
    for job in follow_ups:
        print(
            f"\nID: {job[0]}, Company: {job[1]}, Title: {job[2]}, Follow-up: {job[4]}"
        )


def main():
    """Main CLI loop."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_job()
        elif choice == "2":
            view_all_jobs()
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_job()
        elif choice == "5":
            view_upcoming_follow_ups()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
