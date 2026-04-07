import math

class Shape:
    def area(self):
        ...

    def perimeter(self):
        ...

    def __str__(self):
        return f"\tArea: {self.area():.2f}\n\tPerimeter: {self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than 0")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return "Circle:\n" + super().__str__()


class Rectangle(Shape):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be greater than 0")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def __str__(self):
        return "Rectangle:\n" + super().__str__()


class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangle sides must be greater than 0")
        if a + b <= c or b + c <= a or a + c <= b:
            raise ValueError("Invalid values for a triangle")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        value = s * (s - self.a) * (s - self.b) * (s - self.c)

        if value < 0 and abs(value) < 1e-10:
            value = 0
        
        return math.sqrt(value)
    
    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return "Triangle:\n" + super().__str__()


def get_positive_number(prompt=""):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    radius = get_positive_number("Radius: ")
    circle = Circle(radius)

    length = get_positive_number("Rectangle length: ")
    width = get_positive_number("Rectangle width: ")
    rectangle = Rectangle(length, width)

    while True:
        a = get_positive_number("Triangle first side: ")
        b = get_positive_number("Triangle second side: ")
        c = get_positive_number("Triangle third side: ")
        
        try:
            triangle = Triangle(a, b, c)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    print(circle)
    print(rectangle)
    print(triangle)


if __name__ == "__main__":
    main()
