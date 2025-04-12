import random

N_NUMBERS: int = 10  # Number of random numbers to generate
MIN_VALUE: int = 1    # Minimum value in the range
MAX_VALUE: int = 100  # Maximum value in the range

def main():
    # Generate and print 10 random numbers between MIN_VALUE and MAX_VALUE
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")  # Print each number on the same line
    print()  # Print a new line at the end

if __name__ == '__main__':
    main()
