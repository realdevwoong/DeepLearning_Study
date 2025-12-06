class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node


  def pop(self):
    if self.is_empty():
      raise IndexError("Pop from empty stack")
    last_data = self.head.data
    self.head = self.head.next
    return last_data
  
  def top(self):
    if self.is_empty():
      raise IndexError("Top from empty stack")
    return self.head.data
  
  def show(self):
    current_data = self.head
    while current_data:
      print(current_data.data, end=" ")
      current_data = current_data.next
  def is_empty(self):
    return self.head is None


stack = Stack()
arr = [10,20,30,40,50]

for x in arr:
  stack.push(x)
stack.show()
print()


while not stack.is_empty():
  print(stack.pop())