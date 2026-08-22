# Keep as it is

import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "output.txt")

sys.stdout = open(output_path, "w", buffering=1)

# Driver code

from shape import Circle, Square, Triangle

circle1 = Circle("red", True, 5)
circle2 = Circle("blue",False,9)
square = Square("blue", True, 10)
triangle = Triangle("yellow", False, 18, 9)

circle1.describe()
circle2.describe()
square.describe()
triangle.describe()

# injecting matplotlib to make things interesting!

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# take note of any() here - returns False only when all are False in a sequence

if any(isinstance(v, (Circle, Square, Triangle)) for v in list(locals().values())):

    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    for name, obj in list(locals().items()):
        if isinstance(obj, (Circle, Square, Triangle)):
            fig, ax = plt.subplots()
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_aspect('equal')    
            if isinstance(obj, Circle):
                # ternary operator used for facecolor
                circle_patch = patches.Circle((0.5, 0.5), obj.radius/20, edgecolor=obj.color, facecolor=obj.color if obj.is_filled else 'none', linewidth=2)
                ax.add_patch(circle_patch)
            if isinstance(obj, Square):
                size = obj.side / 10
                square_patch = patches.Rectangle((0.5 - size/2, 0.5 - size/2), size, size, edgecolor=obj.color, facecolor=obj.color if obj.is_filled else 'none', linewidth=2)
                ax.add_patch(square_patch)

plt.show()