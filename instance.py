# Importing necessary classes from toy.py and toyStore.py modules
from toy import StuffedToy, ElectronicToy
from toyStore import ToyArea, ToyStore

# Creating instances of ToyArea and ToyStore
toy_area = ToyArea()  # Create a ToyArea instance to represent the area where toys are stored
toy_store = ToyStore()  # Create a ToyStore instance to represent the store where toys are sold

# Adding toys to the toy area
toy_area.add_toy(StuffedToy("Teddy Bear", "Brown"))
toy_area.add_toy(StuffedToy("Unicorn", "White"))  
toy_area.add_toy(ElectronicToy("Robot", "AA"))  
toy_area.add_toy(ElectronicToy("Phone", "AA"))  

# Buying toys from the toy store
toy_store.buy_toy(StuffedToy("Panda", "White and Black"))
toy_store.buy_toy(ElectronicToy("Car Toy", "AAA"))  
toy_store.buy_toy(ElectronicToy("Phone", "AA"))  