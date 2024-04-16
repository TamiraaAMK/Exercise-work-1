import random

class Kid:
    def __init__(self, name):
        # Initialize Kid object with a name, current toy set to None, and an empty list of toys
        self.name = name
        self.current_toy = None
        self.toys = []

    def play_with_toy(self, toy):
        # Method to play with a toy
        if self.current_toy:
            self.return_to_toy_area()  # If the kid is already playing with a toy, return it to the toy area
        print(f"{self.name} is playing with {toy.name}.")  # Print the kid's name and the toy they are playing with
        toy.play()  # Call the play method of the toy
        self.current_toy = toy  # Set the current toy to the one being played with

    def stop_playing(self):
        # Method to stop playing with the current toy
        if self.current_toy:
            print(f"{self.name} stops playing with {self.current_toy.name}.")  # Print the kid's name and the toy they stopped playing with
            self.current_toy = None  # Set the current toy to None
        else:
            print(f"{self.name} is not playing with any toy.")  # Print if the kid is not playing with any toy

    def decide_from_toy(self, toy_area):
        # Method for the kid to decide which toy to play with
        print(f"{self.name} is deciding from a toy.")
        if not toy_area.toys:
            print("Toy area is empty.")  # Print if the toy area is empty
            return
        chosen_toy = random.choice(toy_area.toys)  # Choose a random toy from the toy area
        print(f"{self.name} chooses {chosen_toy.name}.")  # Print the kid's name and the chosen toy
        return chosen_toy

    def add_toy(self, toy):
        # Method to add a toy to the kid's collection
        print(f"{self.name} adds {toy.name} to the collection.")  # Print the kid's name and the toy being added
        self.toys.append(toy)  # Add the toy to the list of toys

    def return_to_toy_area(self):
        # Method to return the current toy to the toy area
        if self.current_toy:
            print(f"{self.name} returns {self.current_toy.name} to the toy area.")  # Print the kid's name and the toy being returned
            self.current_toy = None  # Set the current toy to None

    def buy_toy(self, toy_store, toy):
        # Method for the kid to buy a toy from the store
        if toy in toy_store.toys:
            print(f"{self.name} buys {toy.name} from the store.")  # Print the kid's name and the toy being bought
            toy_store.sell_toy(toy)  # Sell the toy from the store
            self.stop_playing()  # Stop playing with the current toy
            self.return_to_toy_area()  # Return the current toy to the toy area
            self.add_toy(toy)  # Add the bought toy to the kid's collection
        else:
            print(f"{toy.name} is not available in the store.")  # Print if the toy is not available in the store

    def is_playing(self):
        # Method to check if the kid is playing
        return random.choice([True, False])  # Return a random boolean value
