"""
16. Function Decorators
Assignment:
Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().
"""


def log_function_call(func):  # Decorator function
    def wrapper():
        print("Function is being called")  # Before executing the function
        func()  # Calling the function
    return wrapper


@log_function_call  # Applying decorator to the function
def say_hello():
    print("Hello")


# Calling the decorated function
say_hello()
