# Abstract class

# Cannot have objects of its own
# Can only be Parent class
# Child classes must use all the abstract methods defined in the abstract class that they inherit
# Use of decorator to declare abstract methods
# Must import ABC and abstractmethod
# ABC = Abstract Base Class

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")