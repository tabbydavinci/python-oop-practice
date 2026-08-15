# Keep as it is

import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "output.txt")

sys.stdout = open(output_path, "w", buffering=1)

# Driver code

from animal import Dog, Cat

dog = Dog("Rocky")
cat = Cat("Kitty")

dog.eat()
dog.sleep()
dog.speak()

print()

cat.eat()
cat.sleep()
cat.speak()