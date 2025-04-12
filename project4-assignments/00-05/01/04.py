import math  # Import the math library so we can use the sqrt function

def main():
    # Get the two side lengths from the user and convert them to floats
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the Pythagorean theorem
    bc: float = math.sqrt(ab**2 + ac**2)

    # Display the result using an f-string for cleaner formatting
    print(f"The length of BC (the hypotenuse) is: {bc}")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
