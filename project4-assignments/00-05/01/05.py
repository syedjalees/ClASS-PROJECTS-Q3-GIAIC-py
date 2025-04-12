def main():
    # Get the numbers to divide
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Perform integer division and calculate the remainder
    quotient: int = dividend // divisor  # Integer division (quotient)
    remainder: int = dividend % divisor  # Modulo operation (remainder)
    
   
    print(f"The result of this division is {quotient} with a remainder of {remainder}")


if __name__ == '__main__':
    main()
