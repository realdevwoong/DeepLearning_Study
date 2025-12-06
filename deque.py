from collections import deque


d = deque()
arr = [6,7,8,9,10]
for x in arr:
  d.append(x)
arr = [5,4,3,2,1]
for x in arr:
  d.appendleft(x)

print(d)

while d:
  print(d.popleft(), end=" ")
print()

arr = [1,2,3,4,5]
for x in arr:
  d.appendleft(x)
print(d)
while True:
  print(d.pop(), end=" ")
  if not d:
    break
  print(d.popleft(), end=" ")
  if not d:
    break
print()