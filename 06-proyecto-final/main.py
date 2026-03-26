# Starting with the import statements:
# We will import the necessary modules that we will use in our main function.

from menu import show_menu
from orders import order_coffee
from order_history import view_order_history

"""
This block of code contains several modules
that are used in the main function of the program. 

Each module is responsible for a specific task, 
such as handling user input, processing orders, and managing the order history. 

The main function serves as the entry point of the program, 
where it displays a menu to the user and allows them to choose an option 
to either order a coffee or view their order history.
"""

def main():
    # This while loop will run indefinitely until the user decides to exit the program
    while True:
        # Call the module in order to show menu options to the user
        show_menu()
        option = input("\n-> Please choose an option: ")

        if option == '1':
            # Call the module to order a coffee
            order_coffee()

        elif option == '2':
            # View the history of orders
            view_order_history()

        elif option == '3':
            print("\nThank you for using the program. Goodbye!")
            break # Exit the loop and end the program

        else:
            print("Invalid option. Please try again.")

# Next, we check if this script is being run directly (as the main program) and if so, we call the main function to start the program.
# That way, we stablish the principal entry point of the program, allowing it to run when executed directly.
if __name__ == "__main__":
    main()