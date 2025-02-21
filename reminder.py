from plyer import notification
from database import get_upcoming_follow_ups
import schedule
import time


def send_notification(title, message):
    """Send a desktop notification."""
    notification.notify(title=title, message=message, timeout=10)


def check_follow_ups():
    """Check for upcoming follow-ups and send notifications."""
    follow_ups = get_upcoming_follow_ups(1)  # Check for follow-ups within 1 day
    for job in follow_ups:
        message = f"Follow-up for {job[1]} ({job[2]}) is due on {job[4]}."
        send_notification("Job Follow-up Reminder", message)


def start_reminder_scheduler():
    """Start the scheduler to check for follow-ups."""
    schedule.every().day.at("09:00").do(check_follow_ups)
    while True:
        schedule.run_pending()
        time.sleep(1)
