def main():
    for i in range(10, 20):  # Loop through numbers from 10 to 19
        if is_odd(i):  # Check if the current number is odd
            print(f"{i} odd")
        else:  # Otherwise, it's even
            print(f"{i} even")

def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    return value % 2 != 0  # Returns True if the number is odd (not divisible by 2)

if __name__ == '__main__':
    main()
