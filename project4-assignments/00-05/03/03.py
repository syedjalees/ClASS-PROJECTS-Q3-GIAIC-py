def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    # Check leap year conditions
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year!")
            else:
                print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year.")


# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
