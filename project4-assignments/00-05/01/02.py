C = 299792458  # The speed of light in m/s

def main():
    # Prompt the user for mass in kilograms
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using Einstein's formula
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display the calculations and results to the user
    print("e = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules} joules of energy!")


if __name__ == '__main__':
    main()
