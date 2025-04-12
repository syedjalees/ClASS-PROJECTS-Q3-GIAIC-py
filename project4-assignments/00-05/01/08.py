SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "  # adjective noun verb

def main():
    # Get the three inputs from the user to create the Mad Lib sentence
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Print the completed sentence using f-string for cleaner formatting
    print(f"{SENTENCE_START}{adjective} {noun} {verb}!")

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
