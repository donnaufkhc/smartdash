import time
import threading
import win10toast
from datetime import datetime, timedelta

class SmartDash:
    def __init__(self):
        self.toaster = win10toast.ToastNotifier()
        self.alerts = []

    def add_alert(self, title, message, alert_time):
        """Add a new alert."""
        alert_time = datetime.strptime(alert_time, "%Y-%m-%d %H:%M:%S")
        self.alerts.append((title, message, alert_time))
        print(f"Added alert: '{title}' at {alert_time}")

    def check_alerts(self):
        """Check and notify for any alerts that are due."""
        while True:
            now = datetime.now()
            for alert in self.alerts:
                title, message, alert_time = alert
                if now >= alert_time:
                    self.toaster.show_toast(title, message, duration=10)
                    self.alerts.remove(alert)
            time.sleep(60)  # Check every minute

    def start(self):
        """Start the alert checking process."""
        alert_thread = threading.Thread(target=self.check_alerts)
        alert_thread.daemon = True
        alert_thread.start()
        print("SmartDash is running. Press Ctrl+C to exit.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("SmartDash stopped.")

if __name__ == "__main__":
    smart_dash = SmartDash()
    # Example usage:
    # smart_dash.add_alert("Meeting Reminder", "Team meeting at 10 AM", "2023-10-25 10:00:00")
    smart_dash.start()