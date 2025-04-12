def main():

    curr_value = int(input("Enter a number: "))
    
    
    while curr_value < 100:
        # Double the value
        curr_value = curr_value * 2
        # Print the current doubled value
        print(curr_value, end=" ")

if __name__ == '__main__':
    main()
