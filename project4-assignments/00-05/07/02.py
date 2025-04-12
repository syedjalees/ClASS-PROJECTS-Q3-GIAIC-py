# n: the number to check.
# low: the lower bound of the range.
# high: the upper bound of the range.

def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    # Example usage
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    # Call the in_range function and print the result
    print(in_range(n, low, high))

if __name__ == '__main__':
    main()
