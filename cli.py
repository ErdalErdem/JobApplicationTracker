import argparse
from colorama import Fore, Style, init
from database import (
    add_job_application,
    get_all_job_applications,
    update_job_status,
    delete_job_application,
    get_upcoming_follow_ups,
)

# Initialize colorama
init(autoreset=True)


def display_menu():
    """Display the CLI menu with colors."""
    print(Fore.CYAN + "\n=== Job Application Tracker ===")
    print(Fore.GREEN + "1. Add Job Application")
    print(Fore.GREEN + "2. View All Job Applications")
    print(Fore.GREEN + "3. Update Job Status")
    print(Fore.GREEN + "4. Delete Job Application")
    print(Fore.GREEN + "5. View Upcoming Follow-ups")
    print(Fore.RED + "6. Exit")
    print(Fore.CYAN + "==============================")


def add_job():
    """Add a new job application with colored prompts."""
    print(Fore.YELLOW + "\n=== Add Job Application ===")
    company_name = input(Fore.BLUE + "Enter company name: " + Style.RESET_ALL)
    job_title = input(Fore.BLUE + "Enter job title: " + Style.RESET_ALL)
    date_applied = input(
        Fore.BLUE + "Enter date applied (YYYY-MM-DD): " + Style.RESET_ALL
    )
    follow_up_date = input(
        Fore.BLUE + "Enter follow-up date (YYYY-MM-DD): " + Style.RESET_ALL
    )
    status = input(
        Fore.BLUE
        + "Enter status (Applied, Interview, Offer, Rejected, etc.): "
        + Style.RESET_ALL
    )
    notes = input(Fore.BLUE + "Enter notes: " + Style.RESET_ALL)
    add_job_application(
        company_name, job_title, date_applied, follow_up_date, status, notes
    )
    print(Fore.GREEN + "Job application added successfully!")


def view_all_jobs():
    """View all job applications with colored output."""
    jobs = get_all_job_applications()
    print(Fore.YELLOW + "\n=== All Job Applications ===")
    for job in jobs:
        print(
            Fore.CYAN + f"\nID: {job[0]}, "
            f"Company: {Fore.GREEN}{job[1]}, "
            f"Title: {Fore.MAGENTA}{job[2]}, "
            f"Applied: {Fore.YELLOW}{job[3]}, "
            f"Follow-up: {Fore.YELLOW}{job[4]}, "
            f"Status: {Fore.BLUE}{job[5]}, "
            f"Notes: {Fore.WHITE}{job[6]}"
        )
    print(Fore.YELLOW + "============================")


def update_status():
    """Update the status of a job application with colored prompts."""
    print(Fore.YELLOW + "\n=== Update Job Status ===")
    job_id = input(Fore.BLUE + "Enter job ID to update: " + Style.RESET_ALL)
    new_status = input(Fore.BLUE + "Enter new status: " + Style.RESET_ALL)
    update_job_status(job_id, new_status)
    print(Fore.GREEN + "Job status updated successfully!")


def delete_job():
    """Delete a job application with colored prompts."""
    print(Fore.YELLOW + "\n=== Delete Job Application ===")
    job_id = input(Fore.BLUE + "Enter job ID to delete: " + Style.RESET_ALL)
    delete_job_application(job_id)
    print(Fore.RED + "Job application deleted successfully!")


def view_upcoming_follow_ups():
    """View upcoming follow-ups with colored output."""
    days = input(
        Fore.BLUE + "Enter number of days to check for follow-ups: " + Style.RESET_ALL
    )
    follow_ups = get_upcoming_follow_ups(days)
    print(Fore.YELLOW + f"\n=== Upcoming Follow-ups (Next {days} Days) ===")
    for job in follow_ups:
        print(
            Fore.CYAN + f"\nID: {job[0]}, "
            f"Company: {Fore.GREEN}{job[1]}, "
            f"Title: {Fore.MAGENTA}{job[2]}, "
            f"Follow-up: {Fore.YELLOW}{job[4]}"
        )
    print(Fore.YELLOW + "============================")


def main():
    """Main CLI loop with colored interface."""
    while True:
        display_menu()
        choice = input(Fore.BLUE + "Enter your choice: " + Style.RESET_ALL)
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
            print(Fore.RED + "\nExiting the Job Application Tracker. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
