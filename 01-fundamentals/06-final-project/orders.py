# Declering a constant for the order history file
ORDER_HISTORY = "order_history.txt"

# Starting with the menu variety
def order_coffee():
    print("\nThese are the available coffee options:")
    print("1. Latte")
    print("2. Espresso")
    print("3. Americano")
    print("4. Cappuccino")

    option = input("\n-> What would you like to order? ")

    # Using a dictionary to map the user's choice to the corresponding coffee type
    coffeeType = {
        '1': 'Latte',
        '2': 'Espresso',
        '3': 'Americano',
        '4': 'Cappuccino'
    }

    # Check if the user's choice is valid and print the selected coffee type
    if option in coffeeType:
        selected_coffee = coffeeType[option] # Get the coffee type from the dictionary
        print("\nYou have ordered a: " + selected_coffee)
        print("Please wait while we prepare your coffee...")
        print("Your " + selected_coffee + " is ready! Enjoy! :)")
    
        # Append let us add the new order to the order history file without overwriting the existing orders
        with open(ORDER_HISTORY, "a", encoding="utf-8") as file: 
            file.write(selected_coffee + "\n") 
    else:
        print("Invalid option. Please try again.")



