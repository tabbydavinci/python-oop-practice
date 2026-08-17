# Super method - for attributes or methods that child classes have in common

# super().describe() - inplace runs the describe() method of parent class wherever called inside a child class's method

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"{self.color} {type(self).__name__}, fill {self.is_filled}", end="")

class Circle(Shape):
    
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f", {self.radius} cm radius")

class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side

    def describe(self):
        super().describe()
        print(f", {self.side} cm side")

class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height

    def describe(self):
        super().describe()
        print(f", {self.base} cm base, {self.height} cm height")