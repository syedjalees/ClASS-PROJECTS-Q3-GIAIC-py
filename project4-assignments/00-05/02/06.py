def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    print(lst[-1])  # Using Python's negative indexing to get the last element


def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":  # Keep asking until the user presses Enter with no input
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst  # Return the created list

def main():

    lst = get_lst()

    
    get_last_element(lst)


if __name__ == '__main__':
    main()
