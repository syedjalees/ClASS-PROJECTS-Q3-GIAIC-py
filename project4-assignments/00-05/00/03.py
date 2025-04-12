def main():
    
    fahrenheit: float = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius using the given formula
    celsius: float = (fahrenheit - 32) * 5.0 / 9.0

    # Output the temperature in both Fahrenheit and Celsius
    print(f"Temperature: {fahrenheit}F = {celsius}C")



if __name__ == '__main__':
    main()
