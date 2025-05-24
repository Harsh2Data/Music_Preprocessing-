import time
import pyttsx3
from plyer import notification
from datetime import datetime

# Voice Engine Setup
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Your Reminder List
reminders = [
    {"text": "Drink Water", "interval": 60 * 60},  # every 1 hour
    {"text": "Eat Food", "interval": 4 * 60 * 60},  # every 4 hours
    {"text": "Take a 5-min break", "interval": 90 * 60}  # every 1.5 hours
]

# Last run time storage
last_triggered = {reminder["text"]: time.time() - reminder["interval"] for reminder in reminders}

# Today’s tasks (Optional To-do)
todo_list = [
    "✅ Complete NumPy Practice",
    "✅ 1 hour Gym",
    "✅ Apply for next Coursera course"
]

def show_todo():
    print("\n📋 Today’s To-Do List:")
    for task in todo_list:
        print(task)

def remind(task):
    # Notification
    notification.notify(
        title="🤖 JARVIS Reminder",
        message=task,
        timeout=5
    )
    speak(task)

# Main Loop
try:
    print("✅ JARVIS Reminder Started")
    show_todo()
    while True:
        current_time = time.time()
        for reminder in reminders:
            if current_time - last_triggered[reminder["text"]] >= reminder["interval"]:
                remind(reminder["text"])
                last_triggered[reminder["text"]] = current_time
        time.sleep(10)

except KeyboardInterrupt:
    print("⛔ Reminder Bot Stopped")
