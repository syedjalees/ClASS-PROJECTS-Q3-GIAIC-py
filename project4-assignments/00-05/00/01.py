def main():
    print("This program adds two numbers.")

    num1_input: str = input("Enter first number: ")
    num1: int = int(num1_input)  # Convert to integer


    num2_input: str = input("Enter second number: ")
    num2: int = int(num2_input)  # Convert to integer

    # Calculate sum
    total: int = num1 + num2

    # Display result
    print(f"The total is {total}.")


# Python file to call the main() function.
if __name__ == '__main__':
    main()
