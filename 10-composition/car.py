# Composition - composed object directly owns its component objects which cannot exist independent of composed object

# owns-a relationship

# if I were to delete the Car object then the engine, bodywork and wheels would also cease to exist

# because the Engine, Bodywork and Wheel objects are created inside the Car object rather than passed from outside

# component objects
class Engine:
    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower

class Bodywork:
    def __init__(self, material, colour):
        self.material = material
        self.colour = colour

class Wheel:
    def __init__(self, category, wheel_size):
        self.category = category
        self.wheel_size = wheel_size

# composed object
class Car:
    def __init__(self, make, model, engine_type, horsepower, material, colour, category, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(engine_type, horsepower)
        self.bodywork = Bodywork(material, colour)
        self.wheel = [Wheel(category, wheel_size) for wheel in range(4)]

    def display(self):
        print(f"This is a {self.make} {self.model} with {self.bodywork.colour} {self.bodywork.material} bodywork, {self.engine.horsepower}(hp) {self.engine.engine_type} engine, and {self.wheel[0].wheel_size} in. {self.wheel[0].category} wheels")