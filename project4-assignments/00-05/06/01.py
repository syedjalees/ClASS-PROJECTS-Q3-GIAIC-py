import random

# Define the likelihood of done() returning True
DONE_LIKELIHOOD = 0.5  # Adjust this value for higher or lower chances of stopping early

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Exit the function if done() returns True
        print(curr_num)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
