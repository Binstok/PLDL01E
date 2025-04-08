class Pet:
    def __init__(self, name):
        # Initialize private attributes
        self.__name = name    # Pet's name (string)
        self.__hunger = 5     # Hunger level (0-10, default 5)
        self.__energy = 5     # Energy level (0-10, default 5)

    def feed(self):
        self.__hunger = max(0, self.__hunger - 1)
        print(f"{self.__name} was fed. Hunger decreased.")

    def play(self):
        self.__energy = max(0, self.__energy - 1)
        self.__hunger = min(10, self.__hunger + 1)
        print(f"{self.__name} played. Energy decreased, hunger increased.")

    def rest(self):
        self.__energy = min(10, self.__energy + 2)
        print(f"{self.__name} rested. Energy increased.")

    def status(self):
        print(f"\n{self.__name}'s Status:")
        print(f"• Hunger: {self.__hunger}/10")
        print(f"• Energy: {self.__energy}/10")

# Demonstration
if __name__ == "__main__":
    # Create a pet
    my_pet = Pet("Fluffy")

    # Initial status
    print("=== Virtual Pet Simulator ===")
    my_pet.status()  # Expected: Hunger:5, Energy:5

    # Test feed()
    my_pet.feed()    # Hunger → 4
    my_pet.status()  # Verify

    # Test play()
    my_pet.play()    # Energy → 4, Hunger → 5
    my_pet.status()  # Verify

    # Test rest()
    my_pet.rest()    # Energy → 6
    my_pet.status()  # Final status