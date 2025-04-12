def main():
    lst = []  # Create an empty list to store user input


    while True:
        val = input("Enter a value: ")  
        if val == "":  
            break  # Exit the loop if the user presses Enter without input
        lst.append(val)  # Add the value to the list

    # Print the final list
    print(f"Here's the list: {lst}")



if __name__ == '__main__':
    main()
