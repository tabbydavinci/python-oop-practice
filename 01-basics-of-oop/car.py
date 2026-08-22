# Basics of OOP

class Car:
    def __init__(self,make,model,year,color,for_sale):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def describe(self):
        if self.for_sale:
            print(f"Here's a {self.year} {self.color} {self.make} {self.model} that is For Sale!")
        else:
            print(f"Here's a {self.year} {self.color} {self.make} {self.model} that is NOT for sale!")

    def drive(self):
        print(f"That {self.color} {self.model} is driving")

    def stop(self):
        print(f"This {self.color} {self.model} is stopped")