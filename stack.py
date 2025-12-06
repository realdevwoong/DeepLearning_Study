from networkx import is_empty


class Stack:
  def __init__(self):
    self.item = []
  
  def is_empty(self):
    return len(self.item) == 0
  
  def push(self,data):
    self.item.append(data)
  
  def pop(self):
    if self.is_empty():
      raise IndexError("Pop from empty stack")
    return self.item.pop()
  
  def top(self):
    if self.is_empty():
      raise IndexError("Top from empty stack")
    return self.item[-1]
  
stack = Stack()
arr = [9, 7, 8, 6, 4]

for x in arr:
  stack.push(x)

while not stack.is_empty():
  print(stack.pop())
