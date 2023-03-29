class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Finding a specific value in the tree
    def find_value(self, value):
        if self.data == value:
            return self
        elif value < self.data and self.left:
            return self.left.find_value(value)
        elif value > self.data and self.right:
            return self.right.find_value(value)
        return None

root = Node(50)
root.insert(15)
root.insert(35)
root.insert(10)
root.insert(40)
root.insert(5)
root.insert(25)

node = root.find_value(40)
if node:
    print("Found node with value", node.data)
else:
    print("Value not found in tree")

node = root.find_value(75)
if node:
    print("Found node with value", node.data)
else:
    print("Value not found in tree")