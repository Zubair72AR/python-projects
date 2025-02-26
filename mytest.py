import time


def countdown_timer(seconds):
    print("\n⏱️ Countdown Started!\n")
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ {timer} ⏳", end="")
        time.sleep(1)
        seconds -= 1
    print("\n🚨 Time's up! ⏰")


try:
    time_in_seconds = int(input("⏲️ Enter time in seconds: "))
    countdown_timer(time_in_seconds)
except ValueError:
    print("⚠️ Please enter a valid number.")
