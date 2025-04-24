"""
2. Using cls
Assignment:
Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.
"""


class Counter:  # Class
    count = 0  # Save TOTAL OBJECT COUNT in (Class) Variable

    def __init__(self, country_name, dial_num):  # Initialize via a Constructor
        self.country_name = country_name  # Save NAME in (Instance) Variable
        self.dial_num = dial_num  # Save DIAL
        Counter.count += 1  # Increment Class Variable
        self.my_serial = Counter.count  # Store serial number for each object

    def country_details(self):  # Instance Method
        # Print Details
        print(f"{self.my_serial}. {self.country_name}, +{self.dial_num}.")

    @classmethod
    def total_obj(cls):  # Class Method
        if cls.count == 0:
            print("No countries have been added yet.")
        elif cls.count == 1:
            print(f"There is currently {cls.count} country in the list.")
        else:
            print(f"There are {cls.count} countries in total.")


# Creating Instances for Checking Total Number of Objects are created
c1 = Counter("Pakistan", 92)
c2 = Counter("UAE", 971)
c3 = Counter("Qatar", 974)
c4 = Counter("KSA", 966)
c5 = Counter("Iran", 98)

# Call each object’s details
c1.country_details()
c2.country_details()
c3.country_details()
c4.country_details()
c5.country_details()

# Check the Count
Counter.total_obj()
