# Keep as it is

import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "output.txt")
sys.stdout = open(output_path, "w", buffering=1)

# Driver code

from shape import Pizza, Circle, Square, Triangle

# each of the shapes below have two forms
# like a circle is a Circle and a Shape

circle = Circle(4)

shapes = [circle, Square(5), Triangle(6, 7), Pizza("chicken", 15)]

for shape in shapes:
    print(f"{shape.area()} cm^2")