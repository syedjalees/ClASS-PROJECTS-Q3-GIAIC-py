def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(lst[0])  # Access and print the first element of the list

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":  # Keep asking until the user presses Enter with no input
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst  # Return the created list

def main():
  
    lst = get_lst()
    
    
    get_first_element(lst)

if __name__ == '__main__':
    main() 
