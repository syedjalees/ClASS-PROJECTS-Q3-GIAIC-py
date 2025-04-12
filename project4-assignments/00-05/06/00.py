def average(a: float, b: float):
    """
    Returns the number which is half way between a and b.
    """
    sum = a + b
    return sum / 2

def main():
    # Calculate averages of different pairs of numbers
    avg_1 = average(0, 10)   # Average between 0 and 10
    avg_2 = average(8, 10)   # Average between 8 and 10
    
    # Calculate the average between the two averages
    final = average(avg_1, avg_2)
    
    # Print the results
    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final:", final)
    


if __name__ == '__main__':
    main()
