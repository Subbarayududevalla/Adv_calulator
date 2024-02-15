from proj_calculator.calculator import Calculator # Import the Calculator class from the calculator package
# Define the main function
def main():
    # Create an instance of the Calculator class
    calc = Calculator()
    # Print a welcome message
    print("Welcome to the calculator program.")
    print("You can enter any arithmetic expression with +, -, *, /, and parentheses.")
    print("You can also use the commands quit, clear, history, and result.")
    # Start a while loop
    while True:
        # Prompt the user for input
        expression = input("Enter your expression: ")
        # Check if the input is quit
        if expression == "quit":
            # Break the loop and exit the program
            print("Goodbye!")
            break
        # Check if the input is clear
        elif expression == "clear":
            # Clear the calculator
            calc.clear()
            print("Calculator cleared.")
        # Check if the input is history
        elif expression == "history":
            # Print the history of calculations
            print("History of calculations:")
            print(calc.get_history())
        # Check if the input is result
        elif expression == "result":
            # Print the current result
            print("Current result:")
            print(calc.get_result())
        # Otherwise
        else:
            # Try to evaluate the input as a Python expression
            try:
                # Evaluate the input using the eval function
                value = eval(expression, {"__builtins__": None}, vars(calc))
                # Print the value
                print(value)
            # Except any exception
            except Exception as e:
                # Print the exception message
                print(e)
