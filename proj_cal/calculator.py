
# Define the Calculator class
class Calculator:

    # Initialize the calculator with some variables
    def __init__(self):
        self.history = [] # A list to store the history of calculations
        self.result = 0 # A variable to store the current result

    # A static method to validate the input
    @staticmethod
    def validate(x):
        # Check if the input is a number or not
        if not isinstance(x, (int, float)):
            # Raise a ValueError exception
            raise ValueError(f"{x} is not a valid number")
        # Return the input as a float
        return float(x)

    # A class method to add two numbers
    def add(self, x, y):
        # Validate the input
        x = self.validate(x)
        y = self.validate(y)
        # Calculate the sum
        z = x + y
        # Append the calculation to the history list
        self.history.append(f"{x} + {y} = {z}")
        # Update the current result
        self.result = z
        # Return the sum
        return z

    # A class method to subtract two numbers
    def subtract(self, x, y):
        # Validate the input
        x = self.validate(x)
        y = self.validate(y)
        # Calculate the difference
        z = x - y
        # Append the calculation to the history list
        self.history.append(f"{x} - {y} = {z}")
        # Update the current result
        self.result = z
        # Return the difference
        return z

    # A class method to multiply two numbers
    def multiply(self, x, y):
        # Validate the input
        x = self.validate(x)
        y = self.validate(y)
        # Calculate the product
        z = x * y
        # Append the calculation to the history list
        self.history.append(f"{x} * {y} = {z}")
        # Update the current result
        self.result = z
        # Return the product
        return z

    # A class method to divide two numbers
    def divide(self, x, y):
        # Validate the input
        x = self.validate(x)
        y = self.validate(y)
        # Check if the second argument is zero or not
        if y == 0:
            # Raise a ZeroDivisionError exception
            raise ZeroDivisionError("Cannot divide by zero")
        # Calculate the quotient
        z = x / y
        # Append the calculation to the history list
        self.history.append(f"{x} / {y} = {z}")
        # Update the current result
        self.result = z
        # Return the quotient
        return z

    # A class method to get the history of calculations
    def get_history(self):
        # Return the history list as a string
        return "\n".join(self.history)

    # A class method to get the current result
    def get_result(self):
        # Return the current result as a float
        return float(self.result)

    # A class method to clear the calculator
    def clear(self):
        # Reset the history list and the current result
        self.history = []
        self.result = 0
