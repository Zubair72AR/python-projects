from hashlib import sha256


def login(email, login_info, password_to_check):
    # check if same Email with Required Password
    if login_info[email] == hash_password(password_to_check):
        return True
    return False


def hash_password(password):
    # Convert Password into Hashing
    return sha256(password.encode()).hexdigest()


def main():
    # Email and Hashing Password
    login_info = {
        "pakistan@gmail.com": "e2567312ec53232b5353c2798f8054759ee21b03af967265dd22b4cb4284bc49",
        "karachi@gmail.com": "59edcc61af65e1ccac06dc4a9cde88f9d91b6ef5286b48aeb746031800344705",
        "python@gmail.com": "18885f27b5af9012df19e496460f9294d5ab76128824c6f993787004f6d9a7db"
    }

    # Call Function and Print
    print(login("pakistan@gmail.com", login_info, "Pakistan"))
    print(login("pakistan@gmail.com", login_info, "pakistan"))
    print(login("karachi@gmail.com", login_info, "Karachi"))
    print(login("karachi@gmail.com", login_info, "Lahore"))
    print(login("python@gmail.com", login_info, "Python"))
    print(login("python@gmail.com", login_info, "123456789"))


if __name__ == "__main__":
    main()
