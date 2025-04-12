def double(num: int):
    """
    Returns the result of multiplying num by 2.
    """
    return num * 2

def main():
    # Ask the user to enter a number
    num = int(input("Enter a number: "))  # Convert input to an integer
    # Call the double function
    num_times_2 = double(num)
    # Print the doubled result
    print("Double that is", num_times_2)


if __name__ == '__main__':
    main()

