# Class variables

class Student:

    # These are class variables common for all instances of this class
    school_name = "Moneka High Secondary"
    class_year = 2022
    num_of_students = 0

    def __init__(self, name):
        self.name = name
        # Increments at every new object initialisation
        Student.num_of_students += 1