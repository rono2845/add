# add_numbers.py

def add_numbers(num1, num2):
    """
    Function to add two numbers.
    """
    return num1 + num2

if __name__ == "__main__":
    # Input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Calculate the sum
    result = add_numbers(num1, num2)
    
    # Display the result
    print(f"The sum of {num1} and {num2} is {result}.")
