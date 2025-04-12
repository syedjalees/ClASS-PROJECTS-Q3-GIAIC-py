MAX_LENGTH: int = 3  # Set the maximum desired length of the list

def shorten(lst):
    """Shorten the list by removing elements from the end until it's at MAX_LENGTH."""
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove the last element from the list
        print(f"Removed: {last_elem}")  # Print the removed element

def get_lst():
    """Prompt the user to enter one element of the list at a time and return the resulting list."""
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Keep asking until the user presses Enter with no input
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst  # Return the list created from user input

def main():
    lst = get_lst()  # Get the list from the user
    print("Original list:", lst)  # Print the original list
    shorten(lst)  # Shorten the list
    print("Final list:", lst)  

if __name__ == '__main__':
    main()
