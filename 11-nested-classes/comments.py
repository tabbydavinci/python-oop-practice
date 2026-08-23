# Nested classes

# class Outer:
#     class Inner:
#         pass

# Advantages are:
# Logically group classes that are closely related
# Encapsulates private details that aren't relevant outside the Outer class
# Reduces the possibility of naming conflicts by keeping the namespace clean

# class Employee:
#     print("Details of 1st class")

# class Employee:
#     print("Details of 2nd class")

# The above code prints results from both the classes and thus a naming conflict

# But below code is cleaner

# class Company:
#     class Employee:
#         def view_emp():
#             print("Company Employee")

# class Nonprofit:
#     class Employee:
#         def view_emp():
#             print("Nonprofit Employee")

# Also, python executes class bodies at definition time - that means its body runs when the module (company.py) is imported - see below!

# class C:
#     class E:
#         print("Manual for C.E()")
#         def __init__(self):
#             print("C")

# class N:
#     class E:
#         print("Manual for N.E()")
#         def __init__(self):
#             print("N")