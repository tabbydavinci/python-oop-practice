# Duck Typing - polymorphism without inheritance
# If it looks and quacks like a duck, it is a duck
# Class must fulfill the minimum requirements

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        return "BHOW!"

class Cat(Animal):
    def speak(self):
        return "PURR!"

class Car:
    alive = False
    def speak(self):
        return "HONK HONK!"