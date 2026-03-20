import time

def alarm_clock():
    alarm_time = input("Enter alarm time (HH:MM:SS): ")

    print("⏰ Alarm set...")

    while True:
        current_time = time.strftime("%H:%M:%S")
        print("Current Time:", current_time, end="\r")

        if current_time == alarm_time:
            print("\n🔔 WAKE UP! ALARM RINGING!")
            break

        time.sleep(1)

alarm_clock()