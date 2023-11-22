# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")


# Intermediate class inheriting from Animal
class Mammal(Animal):
    def give_birth(self):
        print("Mammal gives birth")


# Child class inheriting from Mammal
class Dog(Mammal):
    def speak(self):
        print(f"{self.name} says Woof!")


# Example usage
if __name__ == "__main__":
    dog = Dog("Buddy")

    dog.speak()  # Output: Buddy says Woof!
    dog.give_birth()  # Output: Mammal gives birth
