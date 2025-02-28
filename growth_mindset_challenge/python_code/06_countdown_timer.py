import time

# Numbers with emojis
num_to_emoji = {
    "0": "0️⃣", "1": "1️⃣", "2": "2️⃣", "3": "3️⃣", "4": "4️⃣",
    "5": "5️⃣", "6": "6️⃣", "7": "7️⃣", "8": "8️⃣", "9": "9️⃣"
}


def convert_to_emoji(number):
    number_string = str(number)
    emoji = []

    for value in number_string:
        emoji.append(num_to_emoji[value])

    emoji_string = "\u2009".join(emoji)
    return emoji_string


def timer_func(user_input):
    print("\n🌹 Countdown has started now!\n")

    while user_input >= 0:
        # Convert total seconds into days, hours, minutes, and seconds
        days, days_reminder = divmod(user_input, 86400)
        hours, hours_reminder = divmod(days_reminder, 3600)
        minutes, seconds = divmod(hours_reminder, 60)

        # Convert numerical values to emoji format
        days_emoji = convert_to_emoji(f"{days:02d}")
        hours_emoji = convert_to_emoji(f"{hours:02d}")
        minutes_emoji = convert_to_emoji(f"{minutes:02d}")
        seconds_emoji = convert_to_emoji(f"{seconds:02d}")

        # Create the timer string with emoji representations
        timer = f"Day {days_emoji}  : Hrs {hours_emoji}  : Mint {minutes_emoji}  : Sec {seconds_emoji}  "

        # Print the timer dynamically in the same line
        print(f"\r{timer}", end="")

        time.sleep(1)
        user_input -= 1

    # Print message when the countdown reaches zero
    print("\nTime is up now..!\n")


# User input handling with error checking
def play():
    while True:
        try:
            user_input = int(input("⏰ Enter Time here in Seconds: "))
            timer_func(user_input)
            break
        except ValueError:
            print("❌ Please enter a valid number.")


if __name__ == "__main__":
    play()
