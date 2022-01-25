# The stack class represents a stack data structure
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # Append item to the end of the stack
    def push(self, item):
        self.items.append(item)

    # Remove the last item of the stack
    def pop(self):
        return self.items.pop()

    # Get, but don't remove, the last item of the stack
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
print(stack.is_empty())
stack.push(1)
print(stack.is_empty())
item = stack.pop()
print(item)
print(stack.is_empty())

for i in range(0, 6):
    stack.push(i)

print(stack.peek())
print(stack.size())

# Reverse a string
newStack = Stack()
for char in "Reverse":
    newStack.push(char)
reverse = ""
for i in range(len(newStack.items)):
    reverse += newStack.pop()
print(reverse)
