# Nested classes

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self, company_name):
            return f"{self.name} works as a {self.position} at {company_name}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details(self.company_name) for employee in self.employees]