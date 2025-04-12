INCHES_IN_FOOT: int = 12  # There are 12 inches in 1 foot.

def main():
    # Prompt the user for the number of feet and convert it to a float
    feet: float = float(input("Enter number of feet: "))
    
    # Perform the conversion from feet to inches
    inches: float = feet * INCHES_IN_FOOT
    
    # Print the result using f-string for cleaner formatting
    print(f"That is {inches} inches!")


if __name__ == '__main__':
    main()
