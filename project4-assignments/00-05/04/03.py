def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name, price in fruits.items():
        amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))
        total_cost += (price * amount_bought)
    
    print(f"Your total is ${total_cost:.2f}")  # Format to 2 decimal places for currency

if __name__ == '__main__':
    main()
