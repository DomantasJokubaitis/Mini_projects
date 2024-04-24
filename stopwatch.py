import time

try:
    timer_set_to = input("Set the stopwatch time like hh:mm:ss  ")
    hours, minutes, seconds = timer_set_to.split(":")
    secs = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
except ValueError:
    while ValueError:
        timer_set_to = input("Ivalid format! Try again: ")


def seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds

tick = 0.01
x = 100

while secs > 0:
    
    hours, minutes, seconds = seconds_to_time(secs)
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)
    secs -= 1

print("Time ended")