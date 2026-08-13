# Keep as it is

import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "output.txt")

sys.stdout = open(output_path, "w", buffering=1)

# Driver code

from car import Car

car_1 = Car("Chevy","Corvette",1999,"red",True)
car_2 = Car("Ford","Mustang",2021,"orange",False)

car_1.describe()
car_2.describe()

print()

car_1.drive()
car_2.stop()