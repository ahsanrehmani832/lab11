# First parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")


# Second parent class
class Bird:
    def fly(self):
        print("Bird can fly")


# Child class inheriting from both Animal and Bird
class Parrot(Animal, Bird):
    def speak(self):
        print(f"{self.name} says Squawk!")


# Example usage
if __name__ == "__main__":
    parrot = Parrot("Polly")

    parrot.speak()  # Output: Polly says Squawk!
    parrot.fly()    # Output: Bird can fly
