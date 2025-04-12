def main():
    numbers: list[int] = [1, 2, 3, 4]  

    # Use list comprehension to double each element in the list
    numbers = [num * 2 for num in numbers]

    print(numbers)  # This should print the doubled list

if __name__ == '__main__':
    main()
