
employees = [
    {
        "name": "Huy",
        "role": "Waiter",
        "hours": 12,
        "sph": .8,
    },
    {
        "name": "Tung",
        "role": "Cook",
        "hours": 24,
        "sph": 1.5,
    },
    {
        "name": "M. Duc",
        "role": "Manager",
        "hours": 20,
        "sph": 2,
    }
]

employees.append(
    {
        "name": "Don",
        "role": "Waitrt",
        "hours": 12,
        "sph": .9,
    }
)

employees.append(
    {
        "name": "H. Duc",
        "role": "Waiter",
        "hours": 14,
        "sph": .7,
    }    
)

# print(employees)

# Print 3rd Dict
print(employees[2]["sph"])

# Edit 1st
newEmployee = {
    "name": "Huyen",
    "role": "Waitress",
    "hours": 14,
    "sph": 1,
}
employees[0] = newEmployee
print(employees[0])

# Delete Last
employees.pop(len(employees) -1)
print(len(employees))

# Print (whole) List
def fill(til, first):
    return " " *(til -len(str((first))))
for employee in employees:
    print(employee["name"], end= fill(8, employee["name"]))
    print(employee["role"], end= fill(10, employee["role"]))
    print(employee["hours"], end= fill(3, employee["hours"]))
    print(employee["sph"], end= fill(3, employee["sph"]))
    print()

# Calculate Monthly Wage
for employee in employees:
    employee["mWage"] = employee["hours"] *employee["sph"]
    print(employee["mWage"])

# Calc total budget
budget= 0
for emp in employees:
    budget += emp["mWage"]
print(budget) 
