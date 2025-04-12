def get_user_info():
    # Collect user data
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    
    # Return data as a tuple
    return first_name, last_name, email_address

def main():
    # Get the user data
    user_data = get_user_info()
    
    # Print the received user data
    print("Received the following user data:", user_data)

if __name__ == '__main__':
    main()
