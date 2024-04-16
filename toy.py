class Toy:
    def __init__(self, name):
        # Initialize Toy object with a name
        self.name = name

    def play(self):
        # Method to simulate playing with the toy
        print(f"{self.name} is being played.")  # Print a message indicating the toy is being played

class StuffedToy(Toy):
    def __init__(self, name, color):
        # Initialize StuffedToy object with a name and color
        super().__init__(name)
        self.color = color

    def play(self):
        # Method to simulate playing with the stuffed toy
        print(f"{self.color} {self.name} is being hugged.")  # Print a message indicating the stuffed toy is being hugged

    def cuddle(self):
        # Method to simulate cuddling with the stuffed toy
        print(f"{self.name} is being cuddled.")  # Print a message indicating the stuffed toy is being cuddled

class ElectronicToy(Toy):
    def __init__(self, name, battery_type):
        # Initialize ElectronicToy object with a name and battery type
        super().__init__(name)
        self.battery_type = battery_type

    def play(self):
        # Method to simulate playing with the electronic toy
        print(f"{self.name} is powered by {self.battery_type} batteries and is making sounds.")  # Print a message indicating the electronic toy is making sounds
