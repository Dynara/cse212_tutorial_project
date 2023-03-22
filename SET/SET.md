# SET 

A `set` is a data structure that is collection of unordered, unchangeable, and unindexed elements. There are also no duplicate members.  By sets not having a defined order, you cannot refer to elements by index. They can appear in a different order every time. Once a set is created, you are only able to add or remove items from the sets.

## Sets in Python
Implement a `set`:
```python
new_set = set()
```

Add an item to a set, using `add(value)`:
```python
new_set.add(1)
```

Remove the item from a set, using `remove(value)` or `discard(value)`:
```python
new_set = {'A', 'B', 'C'}
remove_a = new_set.remove('A')
print(new_set) #Output: {'B', 'C'}

remove_b = new_set.discard('B')
print(new_set) #Output: {'C'}
```

Find smallest element in the set, use `min` and to find the largest, use `max`:
```python
new_set = {1, 2, 3, 4, 5}

smallest_element = min(new_set)
largest_element = max(new_set)

print(smallest_element) #Output: 1
print(largest_element) #Output: 5
```

Find size of set, using `len` :
```python
set_length = len(new_set)
```

Adding sets together. You can use `union`, `| `, or `update`:
```python
set_1 = {1, 2, 3, 4}
set_2 = {5, 6, 7, 8}

set_3 = set_1.union(set_2)
#OR
set_4 = set_1 | set_2
#OR
set_1.update(set_2)


print(set_3) #Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set_4) #Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set_1) #Output: {1, 2, 3, 4, 5, 6, 7, 8}
```

![Set](https://github.com/Dynara/cse212_tutorial_project/blob/ed2ba36f38fcc831b022fbbab2df06dc76fc4c79/SET/set-img.jpg)

Show only elements that are the same in two sets:
```python
set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {5, 6, 7, 8, 9, 10}

set_3 = intersection(set_1, set_2)
OR
set_4 = set_1 & set_2

print(set_3) #Output: {5, 6}
print(set_4) #Output: {5, 6}
```

Show only the elements that are different in two sets, use `difference`. You can also use `symmetric_difference`:
```python
set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {5, 6, 7, 8, 9, 10}

print(set_1.difference(set_2)) #Output: {1, 2, 3, 4}
print(set_2.difference(set_1)) #Output: {8, 9, 10, 7}

print(set_1.symmetric_difference(set_2)) #Output: {1, 2, 3, 4, 7, 8, 9, 10}
```

Iterate through a `set`, use a `for` loop:
```python
set = {1, 2, 3}
for item in set_1:
    print(item)

#Output: 
1
2
3
```

When a `set` is implemented correctly, the Big O Notation is O(1). 
- O(1) means that the execution time of an algorithm is unrelated to the size of the input.

## Here is a class utilizing the previous operations: ##
```python
class Shopping_List:
    # Initiate sets
    def __init__(self):
        self.to_buy = {'lettuce', 'bacon', 'tomato', 'bread', 'milk', 'eggs', 'bananas'}
        self.in_pantry = {'eggs', 'apples', 'bananas', 'oatmeal'}
    # Add to buy
    def add_to_buy(self, ingredient):
        self.to_buy.add(ingredient)
        return ingredient
    # Find number of items
    def number_of_items_to_buy(self):
        number = len(self.to_buy)
        return number
    # Remove item
    def remove_ingredient_from_buy(self, ingredient):
        do_not_need = self.to_buy.remove(ingredient)
        return do_not_need
    # Find what is in your to buy that is not in pantry
    def not_in_pantry(self):
        return self.to_buy.difference(self.in_pantry)

shopping = Shopping_List()
print(shopping.number_of_items_to_buy()) #Output: 7

shopping.add_to_buy('oranges')
shopping.add_to_buy('pineapples')
shopping.add_to_buy('toilet paper')

print(shopping.number_of_items_to_buy()) #Output: 10

shopping.remove_ingredient_from_buy('toilet paper')
print(shopping.number_of_items_to_buy()) #Output: 9

print(shopping.not_in_pantry()) #Output: {'tomato', 'oranges', 'lettuce', 'milk', 'pineapples', 'bacon', 'bread'}

```


## Problem to Solve
- Print what characters were in both the hobbit and lord of the rings
- Print what characters were in either hobbit or lord of the rings, not both
- You forgot Bard what in the hobbit, so you need to add him
- Gollum found out his true name in lord of the rings, you need to remove Gollum from lord of the rings and add Smeagol
- Print characters that were in both hobbit and lord of the rings

```python
hobbit = {'Bilbo', 'Thorin', 'Smaug', 'Witch-king of Angmar', 'Elrond', 'Galadriel', 'Gandalf', 'Gollum', 'Thranduil', 'Legolas', 'Saruman'}
lord_or_the_rings = {'Aragorn', 'Arwen', 'Elrond', 'Bilbo', 'Boromir', 'Gollum', 'Frodo', 'Galadriel', 'Gandalf', 'Legolas', 'Saruman', 'Witch-king of Angmar'}

# ADD CODE HERE


### Find what characters were in both hobbit and lord of the rings

#Output: {'Galadriel', 'Gandalf', 'Elrond', 'Bilbo', 'Witch-king of Angmar', 'Legolas', 'Gollum', 'Saruman'}


### Find out what characters were in either hobbit or lord of rings, not both

#Output: {'Boromir', 'Smaug', 'Arwen', 'Aragorn', 'Thranduil', 'Thorin', 'Frodo'}


### Print characters that were in both hobbit and lord of the rings

#Output: {'Galadriel', 'Legolas', 'Bilbo', 'Gandalf', 'Elrond', 'Witch-king of Angmar', 'Saruman'}

```


[Set Solution](https://github.com/Dynara/cse212_tutorial_project/blob/ed2ba36f38fcc831b022fbbab2df06dc76fc4c79/SET/set_problem_SOLUTION.py) |  [Home](https://github.com/Dynara/cse212_tutorial_project/blob/ed2ba36f38fcc831b022fbbab2df06dc76fc4c79/README.md)
| [STACK](STACK/STACK.md) | [TREE]() 