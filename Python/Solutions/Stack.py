stack = []
# Insert
stack.append(3)
stack.append(2)
stack.append(1)
# Delete
stack.pop()
print(stack)
stack.append(1)
# But, when you print a stack, make sure you print in reverse order (because the tail is the top)
print(stack[::-1])
