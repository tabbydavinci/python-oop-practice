# Keep as it is

import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "output.txt")
sys.stdout = open(output_path, "w", buffering=1)

# Driver code

from car import Car

car1 = Car("Ford", "Mustang", "inline-4", 250, "steel", "orange", "alloy", 18)

car2 = Car("Chevy", "Nomad", "V6", 300, "carbon-steel", "red-white", "chrome", 17)

car1.display()

print()

car2.display()