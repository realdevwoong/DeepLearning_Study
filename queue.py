class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class queue:
  def __init__(self):
    self.head = None
    self.tail = None

    

  # def enqueue(self, data):
  #   new_node = Node(data)
  #   if self.tail:
  #     self.tail.next = new_node
  #   self.tail = new_node
  #   if not self.head:
  #     self.head = new_node

  def enqueue(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = self.tail.next

  def dequeue(self):
    if self.head is None:
      raise IndexError("Dequeue from empty queue")
    dequeued_data = self.head.data
    self.head = self.head.next
    return dequeued_data
  
  def show(self):
    current_data = self.head
    while current_data:
      print(current_data.data, end=" ")
      current_data = current_data.next
    print()

q = queue()
data_list = [1,2,3,4,5]

for data in data_list:
  q.enqueue(data)

print("Queue contents after enqueuing:")
q.show()

print("Dequeuing elements:")
while q.head is not None:
  print(q.dequeue())


print("Queue contents after dequeuing all elements:")
q.show()
print("Enqueuing new elements:")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.show()