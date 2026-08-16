# Keep as it is

import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "output.txt")

sys.stdout = open(output_path, "w", buffering=1)

# Driver code

from vehicle import Car, Boat

car_1 = Car()
boat_1 = Boat()

car_1.go()
car_1.stop()

print()

boat_1.go()
boat_1.stop()