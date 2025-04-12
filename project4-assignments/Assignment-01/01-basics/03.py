import random

def main():
    # Generate the secret number at random between 1 and 99 (inclusive)
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")

    # Get user's first guess
    guess = int(input("Enter a guess: "))
    
    # Keep asking for guesses until the correct one is entered
    while guess != secret_number:
        if guess < secret_number:  # If the guess is too low
            print("Your guess is too low.")
        else:  # If the guess is too high
            print("Your guess is too high.")
        
        # Prompt for a new guess
        guess = int(input("Enter a new guess: "))
    
    # Congratulate the user when they guess the correct number
    print(f"Congrats! The number was: {secret_number}")

if __name__ == '__main__':
    main()
