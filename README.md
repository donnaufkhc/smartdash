# SmartDash

SmartDash is a Python-based application that allows users to customize and schedule alerts for reminders, appointments, or system events on Windows. It uses the Windows 10 toast notifications to alert users at specified times.

## Features

- **Custom Alerts:** Schedule custom alerts with a title, message, and a specific time.
- **Windows Notifications:** Utilizes Windows 10 toast notifications for non-intrusive alerts.
- **Background Operation:** Runs in the background, continuously checking for the scheduled alerts.

## Requirements

- Python 3.x
- `win10toast` library (for Windows notifications)

You can install the required library using pip:

```bash
pip install win10toast
```

## Usage

1. **Add an Alert:**

   You can add an alert by calling the `add_alert` method with a title, message, and the alert time in the format `YYYY-MM-DD HH:MM:SS`.

   ```python
   smart_dash.add_alert("Meeting Reminder", "Team meeting at 10 AM", "2023-10-25 10:00:00")
   ```

2. **Start SmartDash:**

   Run the script to start SmartDash, which will check for alerts every minute.

   ```bash
   python smartdash.py
   ```

   The application will run in the background and notify you at the scheduled times.

3. **Stop SmartDash:**

   Press `Ctrl+C` in the terminal to stop the application.

## Note

- Make sure your system's time and date are set correctly to ensure accurate alert scheduling.
- This program is designed to run on Windows systems.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [win10toast](https://pypi.org/project/win10toast/) for providing the notification functionality.