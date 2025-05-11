"""
18. Property Decorators: @property, @setter, and @deleter
Assignment:
Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
"""


class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price  # Getter method for price

    @price.setter
    def price(self, value):
        self._price = value  # Setter method to update price

    @price.deleter
    def price(self):
        del self._price  # Deleter method to delete price


# Example Usage
product = Product(100)

# Accessing the price using getter
print(f"Price: {product.price}")

# Updating the price using setter
product.price = 150
print(f"Updated Price: {product.price}")

# Deleting the price
del product.price
