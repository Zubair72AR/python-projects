import time
# Dict for Replacing Number to Emoji
num_emoji_dict = {1: "0️⃣ 1️⃣", 2: "0️⃣ 2️⃣", 3: "0️⃣ 3️⃣", 4: "0️⃣ 4️⃣", 5: "0️⃣ 5️⃣", 6: "0️⃣ 6️⃣", 7: "0️⃣ 7️⃣", 8: "0️⃣ 8️⃣", 9: "0️⃣ 9️⃣", 10: "1️⃣ 0️⃣",
                  }


def launch_countdown():
    # For Loop
    for i in range(10, 0, -1):
        # Print Number in the Emoji Number
        print(num_emoji_dict[i])
        # Delay 1 Second for Countdown Time
        time.sleep(1)
    # Print "🚀 Liftoff!" after Loop Finished
    print("🚀 Liftoff!")


if __name__ == "__main__":
    launch_countdown()
