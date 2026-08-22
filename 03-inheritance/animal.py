# Inheritance

class Animal:

    def __init__(self, name, is_alive=True):
        self.name = name
        self.is_alive = is_alive

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says WOOF!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says MEOW!")