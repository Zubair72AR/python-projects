"""
4. Class Variables and Class Methods
Assignment:
Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.
"""


class Bank:  # Class
    bank_name = "Default Bank"  # Class Variable

    def __init__(self, account_holder: str):  # Constructor
        self.account_holder = account_holder  # Instance Variable

    def display_account(self):  # Instance Method
        print(
            f"Account Holder: {self.account_holder} | Bank: {Bank.bank_name}")

    @classmethod
    def change_bank_name(cls, name: str):  # Class Method
        cls.bank_name = name  # Change Class Variable


# Create some bank accounts
acc1 = Bank("Zubair Ahmed")
acc2 = Bank("Babar Ali")

# Display before changing bank name
acc1.display_account()
acc2.display_account()

# Change the bank name using class method
Bank.change_bank_name("Islamic Bank")

# Display after change
acc1.display_account()
acc2.display_account()
