class Friends:
    # Initiate stack
    def __init__(self):
        self.employees = []

    # Adding items to stack
    def push(self, name):
        self.employees.append(name)
        return name
    
    # Return number of items
    def number_of_employees(self):
        number = len(self.employees)
        return number

    # Return item that was removed from stack
    def pop(self):
        self.employees.pop()
    
    # Return last item in stack
    def peek(self):
        if len(self.employees) == 0:
            return None
        else:
            return self.employees[-1]
    
    def current_employees(self):
        return self.employees

f = Friends()
f.push('Rachel')
f.push('Ross')
f.push('Phoebe')
f.push('Michael')
f.push('Pam')
f.push('Joey')
f.push('Monica')
f.push('Dwight')
f.push('Chandler')
f.push('Jim')

print(f.number_of_employees())

for i in range(7):
    f.pop()

f.push('Joey')
f.push('Monica')
f.push('Chandler')

employees = f.current_employees()
print(employees)

print(f.number_of_employees())

"""
Output:
10
['Rachel', 'Ross', 'Phoebe', 'Joey', 'Monica', 'Chandler']
6
"""





