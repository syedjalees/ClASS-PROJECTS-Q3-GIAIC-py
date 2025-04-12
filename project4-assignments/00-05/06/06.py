def print_divisors(num: int):
    """
    This function prints all divisors of the number `num`.
    """
    print(f"Here are the divisors of {num}")
    # Loop through numbers from 1 to num (inclusive)
    for i in range(1, num + 1):
        if num % i == 0:  # If `i` divides `num` evenly
            print(i, end=" ")

def main():

    num = int(input("Enter a number: "))
 
    print_divisors(num)


if __name__ == '__main__':
    main()
