def calculate_electricity_bill(units):
    if units <= 100:
        bill = 0
    elif units <= 200:
        bill = (units - 100) * 5
    elif units <= 300:
        bill = (100 * 5) + (units - 200) * 10
    else:
        bill = (100 * 5) + (100 * 10) + (units - 300) * 20
    return bill

def main():
    try:
        units_consumed = float(input("Enter the number of electricity units consumed: "))
        if units_consumed < 0:
            print("Invalid input. Please enter a positive value.")
        else:
            bill_amount = calculate_electricity_bill(units_consumed)
            print(f"Monthly Electricity Bill: {bill_amount} rupees")
    except ValueError:
        print("Invalid input. Please enter a valid number of units.")

if __name__ == "__main__":
    main()
