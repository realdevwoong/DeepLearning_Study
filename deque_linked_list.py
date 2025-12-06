from hmac import new


class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None


class Deque:
  def __init__(self):
    self.front = None
    self.rear = None
    self.size = 0

  def append_front(self, data):
    new_node = Node(data)
    if self.front == None:
      self.front = new_node
      self.rear = new_node
    else:
      new_node.next = self.front
      self.front.prev = new_node
      self.front = new_node
    self.size += 1

  def append_rear(self, data):
    new_node = Node(data)
    if self.rear == None:
      self.front = new_node
      self.rear = new_node
    else:
      new_node.prev = self.rear
      self.rear.next = new_node
      self.rear = new_node
    self.size += 1 
  def pop_front(self):
    if self.size == 0:
      return None
    popped_data = self.front.data
    self.front = self.front.next
    if self.front == self.rear.next:
      self.rear = None
    else:
      self.front.prev = None
    self.size -= 1
    return popped_data
  
  def pop_rear(self):
    if self.size == 0:
      return None
    popped_data = self.rear.data
    self.rear = self.rear.prev
    if self.rear == self.front.prev:
      self.front = None
    else:
      self.rear.next = None
    self.size -= 1
    return popped_data
  
  def show(self):
    current_data = self.front
    while current_data:
      print(current_data.data, end=" ")
      current_data = current_data.next
    print()

d = Deque()

arr = [6,7,8,9,10]

for x in arr:
  d.append_rear(x)
d.show()

arr = [5,4,3,2,1]

for x in arr:
  d.append_front(x)
d.show()


while True:
  print(d.pop_rear())
  if d.size == 0:
    break
  print(d.pop_front())
  if d.size == 0:
    break

