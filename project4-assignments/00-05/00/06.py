def main():
    # Ask the user to type a number and convert it to a float
    num: float = float(input("Type a number to see its square: "))

    # Print the square of the number using an f-string for cleaner formatting
    print(f"{num} squared is {num ** 2}")



if __name__ == '__main__':
    main()
