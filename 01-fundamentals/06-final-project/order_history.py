# This module will handle the order history for the coffee ordering program.

ORDER_HISTORY = "order_history.txt"

# Declare  a function to view the order history, which will read the order history file and display the orders to the user. 
def view_order_history():
    print("\n***** Order History *****")
    try:
        print("Here are your previous orders:")
        with open(ORDER_HISTORY, "r", encoding="utf-8") as file:
            orders = file.readlines()
            # Check if there are existing orders in the file
            if orders:
                for i, order in enumerate(orders, start=1): # Enumerate is used to number the orders in the history
                    # Cast the index to a string and then print the order number
                    print("#" + str(i) + ". " + order.strip()) # Strip is used to remove any extra whitespace characters from the order string  
            else: 
                # Empty order history file
                print("There are no previous orders.")
    except FileNotFoundError:
        print("No order history found. Please place an order first.")
        return # Important to return here to avoid trying to read a non-existent file