import pygame
import time
from datetime import datetime
def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def alarm_clock():
    # Get user input for alarm time
    alarm_time = input("Enter the alarm time (HH:MM:SS AM/PM): ")
    
    # Convert alarm time to 24-hour format
    alarm_hour, alarm_minute, alarm_second, alarm_period = alarm_time.split(':')
    alarm_hour = int(alarm_hour)
    alarm_minute = int(alarm_minute)
    alarm_second = int(alarm_second)
    alarm_period = alarm_period.strip()
    
    if alarm_period == "PM" and alarm_hour != 12:
        alarm_hour += 12
    elif alarm_period == "AM" and alarm_hour == 12:
        alarm_hour = 0
    
    # Get current time
    while True:
        current_time = datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        current_second = current_time.second
        
        # Check if alarm time is reached
        if current_hour == alarm_hour and current_minute == alarm_minute and current_second == alarm_second:
            print("Wake up! Wake up!")
            play_sound('audio2.mp3')
            break
        
        # Sleep for 1 second before checking again
        time.sleep(1)

# Run the alarm clock
alarm_clock()
