from cli import main
from reminder import start_reminder_scheduler
import threading

if __name__ == "__main__":
    # Start the reminder scheduler in a separate thread
    reminder_thread = threading.Thread(target=start_reminder_scheduler, daemon=True)
    reminder_thread.start()

    # Start the CLI
    main()
