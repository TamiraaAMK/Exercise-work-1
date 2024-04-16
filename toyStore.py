class ToyArea:
    def __init__(self):
        # Initialize ToyArea object with an empty list of toys
        self.toys = []

    def add_toy(self, toy):
        # Method to add a toy to the toy area
        print(f"Adding {toy.name} to the toy area.")  # Print a message indicating the toy being added
        self.toys.append(toy)  # Append the toy to the list of toys

    def take_toy(self, toy):
        # Method to take a toy from the toy area
        print(f"Taking {toy.name} from the toy area.")  # Print a message indicating the toy being taken
        self.toys.remove(toy)  # Remove the toy from the list of toys
        return toy  # Return the removed toy
    
    def return_toy(self, toy):
        # Method to return a toy to the toy area
        print(f"Returning {toy.name} to the toy area.")  # Print a message indicating the toy being returned
        self.toys.append(toy)  # Append the toy back to the list of toys
        return toy  # Return the toy

    def list_toys(self):
        # Method to list all toys in the toy area
        if not self.toys:
            print("Toy area is empty.")  # Print a message indicating the toy area is empty if there are no toys
        else:
            print("Toys available in the toy area:")  # Print a message indicating the available toys
            for toy in self.toys:
                print(toy.name)  # Print the name of each toy

class ToyStore:
    def __init__(self):
        # Initialize ToyStore object with an empty list of toys
        self.toys = []

    def display_toys(self):
        # Method to display all toys in the toy store
        if not self.toys:
            print("Toy store is empty.")  # Print a message indicating the toy store is empty if there are no toys
        else:
            print("Toys available in the store:")  # Print a message indicating the available toys
            for toy in self.toys:
                print(toy.name)  # Print the name of each toy

    def buy_toy(self, toy):
        # Method to buy a toy from the store
        print(f"Buying {toy.name} from the store.")  # Print a message indicating the toy being bought
        self.toys.append(toy)  # Append the toy to the list of toys in the store

    def sell_toy(self, toy):
        # Method to sell a toy from the store
        print(f"Selling {toy.name} from the store.")  # Print a message indicating the toy being sold
        self.toys.remove(toy)  # Remove the toy from the list of toys in the store
