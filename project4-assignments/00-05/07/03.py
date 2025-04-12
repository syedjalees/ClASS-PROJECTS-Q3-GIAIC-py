def main():

    fruit = input("Enter a fruit: ")
    
    # Get the number of that fruit in stock
    stock = num_in_stock(fruit)
    
    # Check if the fruit is in stock
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

def num_in_stock(fruit):
    """
    Returns the number of fruit Sophia has in stock.
    If the fruit is not in stock, returns 0.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        # This fruit is not in stock.
        return 0

if __name__ == '__main__':
    main()
