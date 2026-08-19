# Keep as it is

import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "output.txt")
sys.stdout = open(output_path, "w", buffering=1)

# Driver code

from animal import Dog, Cat, Car

animals = [Dog(), Cat(), Car()]

for animal in animals:
    print(f"Its alive state is {animal.alive} and it says {animal.speak()}")