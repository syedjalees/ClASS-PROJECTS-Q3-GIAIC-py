def print_multiple(message: str, repeats: int):
    """
    Prints the message a specified number of times.
    """
    for i in range(repeats):
        print(message)

def main():
    # Get input from the user
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the function to print the message
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
