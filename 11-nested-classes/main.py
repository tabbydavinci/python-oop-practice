# Keep as it is

import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "output.txt")
sys.stdout = open(output_path, "w", buffering=1)

# Driver code

from company import Company

company1 = Company("Krusty Krab")
company2 = Company("Chum Bucket")

company1.add_employee("Eugene", "Manager")
company1.add_employee("Spongebob", "Cook")
company1.add_employee("Squidward", "Cashier")

company2.add_employee("Plankton", "Manager")
company2.add_employee("Karen", "Assistant")

print(company1.company_name)
print("-" * 30)

for emp in company1.list_employees():
    print(emp)

print()

print(company2.company_name)
print("-" * 30)

for emp in company2.list_employees():
    print(emp)

# Here are a couple more ways to do the same thing

# print(*(emp for emp in company.list_employees()), sep="\n")

# print(*company.list_employees(), sep="\n")