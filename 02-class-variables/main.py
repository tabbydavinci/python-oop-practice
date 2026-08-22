# Keep as it is

import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "output.txt")

sys.stdout = open(output_path, "w", buffering=1)

# Driver code

from student import Student

student_1 = Student("St Johns")
student_2 = Student("St Nelson")
student_3 = Student("St Denis")

print(f"{Student.school_name} NOTICE BOARD")
print(f"The graduating class of {Student.class_year} has {Student.num_of_students} students namely:")
print(student_1.name)
print(student_2.name)
print(student_3.name)