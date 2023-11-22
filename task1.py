# Parent class
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0  # To be overridden by child classes


# Child class inheriting from Shape
class Square(Shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


# Child class inheriting from Shape
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# Example usage
if __name__ == "__main__":
    square = Square("Square", 5)
    circle = Circle("Circle", 3)

    square_area = square.area()
    circle_area = circle.area()

    print(f"{square.name} Area: {square_area}")  # Output: Square Area: 25
    print(f"{circle.name} Area: {circle_area}")  # Output: Circle Area: 28.26
