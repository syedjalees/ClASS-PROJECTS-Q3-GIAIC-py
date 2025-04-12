ADULT_AGE: int = 18  

def is_adult(age: int):
    """
    Returns True if the person is an adult, otherwise False.
    """
    if age >= ADULT_AGE:
        return True
    return False

def main():
    # Ask the user to input an age
    age = int(input("How old is this person?: "))
    # Call the is_adult function and print the result
    print(is_adult(age))

if __name__ == "__main__":
    main()
