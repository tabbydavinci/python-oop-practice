# Can we call my classes in this outermost main.py? Yes we can!

# The below was possible if the subfolders were named like basics_of_oop and had __init__.py (blank works)
# from basics_of_oop.car import Car
# my_car = Car(arguments as required)

# But another way for unusual folder names is this

import importlib

# makes a regular folder pretend as module
basics_module = importlib.import_module("1-basics-of-oop.car")

# getattr(module_var, ClassName)
Car = getattr(basics_module, "Car")

# then use normally
car1 = Car("Honda", "Civic", 2021, "white", False)

car1.describe()