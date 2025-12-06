class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
      if not self.head:
        self.head = Node(data)
        return
      current = self.head
      while current.next:
        current = current.next
      current.next = Node(data) 
    def display(self):
      print("head", end=" -> ")

      current = self.head
      while current:
          print(current.data, end=" -> ")
          current = current.next

      print("tail")
    def insert(self, data, position):
      new_node = Node(data)
      if position == 0:
        new_node.next = self.head
        self.head = new_node
        return
      current = self.head
      for _ in range(position - 1):
        if current is None:
          raise IndexError("Position out of bounds")
        current = current.next
      new_node.next = current.next
      current.next = new_node


linked_list = LinkedList()
data_list = [1,2,3,4,5]

for data in data_list:
    linked_list.append(data)

linked_list.display()

