from kid import Kid  # Importing the Kid class from the kid.py module
from instance import toy_area, toy_store  # Importing toy_area and toy_store from the instance.py module

# Main program loop
while True:
    print("1: Add Kid")
    print("2: List Toys in Toy Area")
    print("3: Kid Decide from Toy Area")
    print("4: Check if Kid is Playing with Toy")
    print("5: Kid Buy Toy from Store")
    print("6: Exit")

    choice = input("Enter your choice: ")  # Prompting the user to enter their choice

    if choice == "1":
        # Option to add a new kid
        name = input("Enter kid's name: ")  # Prompting the user to enter the kid's name
        kid = Kid(name)  # Creating a new Kid object with the entered name
        print(f"Kid {name} added.")  # Printing a confirmation message
    elif choice == "2":
        # Option to list toys in the toy area
        toy_area.list_toys()  # Calling the list_toys method of the toy_area instance to list the toys
    elif choice == "3":
        # Option for the kid to decide from the toy area
        if 'kid' not in locals():
            print("Please add a kid first.")  # Checking if a kid has been added
            continue
        chosen_toy = kid.decide_from_toy(toy_area)  # Calling the decide_from_toy method of the kid instance
        if chosen_toy:
            toy_area.take_toy(chosen_toy)  # Calling the take_toy method of the toy_area instance
    elif choice == "4":
        # Option to check if the kid is playing with a toy
        if 'kid' not in locals():
            print("Please add a kid first.")  # Checking if a kid has been added
            continue
        if kid.is_playing():  # Calling the is_playing method of the kid instance
            print(f"{kid.name} is playing.")  # Printing a message if the kid is playing
        else:
            print(f"{kid.name} is not playing.")  # Printing a message if the kid is not playing
    elif choice == "5":
        # Option for the kid to buy a toy from the store
        if 'kid' not in locals():
            print("Please add a kid first.")  # Checking if a kid has been added
            continue
        toy_store.display_toys()  # Calling the display_toys method of the toy_store instance
        if not toy_store.toys:
            continue
        toy_choice = input("Enter the name of the toy you want to buy: ")  # Prompting the user to enter the toy they want to buy
        for toy in toy_store.toys:
            if toy.name == toy_choice:
                kid.buy_toy(toy_store, toy)  # Calling the buy_toy method of the kid instance
                toy_area.return_toy(chosen_toy)  # Calling the return_toy method of the toy_area instance
                break
        else:
            print("Toy not found in the store.")  # Printing a message if the toy is not found in the store
    elif choice == "6":
        # Option to exit the program
        print("Exiting program.")  # Printing a message indicating program exit
        break  # Exiting the loop and ending the program
    else:
        print("Invalid choice. Please try again.")  # Printing a message for invalid choices

