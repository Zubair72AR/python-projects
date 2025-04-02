from datetime import datetime

# ZUBAIR AHMED student of GIAIC
# Sir Zia Khan, Ali Aftab Sheikh, Muhammad Bilal
# Sir Ameen Alam, All Teacher and Students of GIAIC


def Eid_Mubarak():
    """Eid Mubarak Greetings"""
    today = datetime.today().strftime("%d-%b-%Y")
    date_str = datetime.today().strftime("%A, %d-%b-%Y")
    print(f"\n{'='*30}")
    print(f"📅 {date_str}")
    print(f"{'='*30}\n")

    if today == "31-Mar-2025":
        print("🌙 Eid Mubarak! 💖")
    elif today == "01-Apr-2025":
        print("🥰 Eid Mubarak Day 2! 💖")
    elif today == "02-Apr-2025":
        print("💕 Eid Mubarak Day 3! 💖")
    else:
        print("SubhanAllah! 🌿 Stay blessed. 💖")


if __name__ == "__main__":
    Eid_Mubarak()
