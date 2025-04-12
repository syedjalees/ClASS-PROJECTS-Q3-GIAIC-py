def subtract_seven(num):
    """
    This function takes a number and subtracts 7 from it.
    """
    num = num - 7
    return num

def main():
    # Initialize the number
    num = 7
    # Call the subtract_seven function
    num = subtract_seven(num)
    # Print the result
    print("This should be zero:", num)

if __name__ == '__main__':
    main()
