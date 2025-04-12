def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
   
    return sum(numbers)

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  
    sum_of_numbers: int = add_many_numbers(numbers)  
    print(sum_of_numbers) 
if __name__ == '__main__':
    main()
