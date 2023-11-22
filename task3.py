# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")


# Child class 1 inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

    def fetch(self):
        print("Dog fetches the ball")


# Child class 2 inheriting from Animal
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

    def scratch(self):
        print("Cat scratches the furniture")


# Example usage
if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    dog.speak()  # Output: Buddy says Woof!
    dog.fetch()  # Output: Dog fetches the ball

    cat.speak()  # Output: Whiskers says Meow!
    cat.scratch()  # Output: Cat scratches the furniture
