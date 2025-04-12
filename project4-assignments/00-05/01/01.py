import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    """
    die1 = random.randint(1, NUM_SIDES)  # Roll first die
    die2 = random.randint(1, NUM_SIDES)  # Roll second die
    total = die1 + die2  # Calculate the sum of the two dice
    print(f"Roll result: {die1} + {die2} = {total}")

def main():
    # Display the initial value of die1 (although it is not used in rolling the dice)
    die1 = 10
    print(f"die1 in main() starts as: {die1}")

    # Simulate rolling the dice three times
    roll_dice()
    roll_dice()
    roll_dice()

    # After rolling, show the initial value of die1 (demonstrating variable scope)
    print(f"die1 in main() is still: {die1}")


if __name__ == '__main__':
    main()
