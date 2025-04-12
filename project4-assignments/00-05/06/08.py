def make_sentence(word, part_of_speech):
    """
    This function takes a word and part_of_speech as input and prints the correct sentence.
    - part_of_speech 0: noun
    - part_of_speech 1: verb
    - part_of_speech 2: adjective
    """
    if part_of_speech == 0:
        # Noun
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
        # Verb
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
        # Adjective
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        # Invalid part_of_speech
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    # Ask user for a word (noun, verb, or adjective)
    word = input("Please type a noun, verb, or adjective: ")
    
    # Ask user to specify the part of speech
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Call the make_sentence function to print the correct sentence
    make_sentence(word, part_of_speech)


if __name__ == '__main__':
    main()
