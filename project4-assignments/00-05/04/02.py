def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty phonebook

    while True:
        name = input("Name: ")
        if name == "":  # Stop if the name is an empty string
            break
        number = input("Number: ")
        phonebook[name] = number  # Store name and number in the dictionary

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name, number in phonebook.items():
        print(f"{name} -> {number}")  # Using f-string for cleaner formatting


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":  # Stop if the user enters an empty string
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook")
        else:
            print(f"{phonebook[name]}")  # Print the phone number


def main():
    phonebook = read_phone_numbers()  
    print_phonebook(phonebook)  # Print all the names and numbers
    lookup_numbers(phonebook)  # Allow the user to look up numbers



if __name__ == '__main__':
    main()
