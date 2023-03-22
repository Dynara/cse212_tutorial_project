# **Stack**


**The Function of Stack**

A stack in a data structure that works with a "Last In, First Out" (LIFO). This is accomplished by removing the most recently added item to the stack. Think of how when you are working in Word, there is the "undo" button. It "takes away" you most recent work. 



**Stack Operations**


Implement a stack:
```python
 stack = [ ]
 ```

Add an item to the stack, using `append()` :
```python
 stack.append(item)
 ```

Remove the item from the stack, using `pop()` :
```python
 remove_item = stack.pop()
 ```

![Stack]()

Return the size of the stack, using `len()` :
```python
 length = len(my_stack)
 ```

Return the most recently added item, using `[-1]` :
```python
 return self.my_stack[-1]
 ```

When a stack is implemented correctly, the Big O Notation is O(1). 
- O(1) means that the execution time of an algorithm is unrelated to the size of the input.
 
> Some problems you can run into when using stacks are memory management and index errors. Stacks can be memory-intensive, especially if you are dealing with large data sets. You may get an error if you are trying to access an item that is not in the stack or trying to `'pop'` from an empty list.

## Here is a class utilizing the previous operations: ##
```python
class Shopping_List:
    # Initiate stack
    def __init__(self):
        self.to_buy = []

    # Adding items to stack
    def push(self, ingredients):
        self.to_buy.append(ingredients)
        return ingredients
    
    # Return number of items
    def number_of_items(self):
        number = len(self.to_buy)
        return number

    # Return item that was removed from stack
    def pop(self):
        return self.to_buy.pop()
    
    # Return last item in stack
    def peek(self):
        return self.to_buy[-1]
    
shopping = Shopping_List()
shopping.push('lettuce')
shopping.push('bacon')
shopping.push('tomato')
shopping.push('bread')

print(shopping.number_of_items())  
print(shopping.pop())
print(shopping.peek())
print(shopping.number_of_items())

"""
Output:
4
bread
tomato
3
"""
```

**Problem to Solve** 
=
- You need to add the following names to the class Friends: Rachel, Ross, Phoebe, Michael, Pam, Joey, Monica, Dwight Chandler, Jim.
- Print number of employees
- After adding everyone, you were told Michael, Pam, Dwight, and Jim left Friends to work at the Office. They need removed from the list of employees. 
- You need to return a list of current employees.
- Print number of employees

```python
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
    
    # Return employees
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

# Add Code Here



"""
Output:
10
['Rachel', 'Ross', 'Phoebe', 'Joey', 'Monica', 'Chandler']
6
"""
```


[Stack Solution](stack_problem_SOLVED.py) | [Home]()
