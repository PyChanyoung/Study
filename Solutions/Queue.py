from collections import deque
# Append / popleft ==> both are O(1)
# List 를 이용해서 queue를 구현하면 맨 앞에놈을 꺼낼때 O(N)이 드는거나 마찬가지다.

queue = deque()
# Insert
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
# Delete
queue.popleft()
print(queue)
