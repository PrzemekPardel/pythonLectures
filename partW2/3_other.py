#stack LIFO
stack = []
stack.append(1)
stack.append(3)
stack.append(9)
print(stack)
stack.pop()
print(stack)

#queue FIFO
from collections import deque #module import
queue = deque()
queue.append(1)
queue.append(3)
queue.append(9)
print(queue)
queue.popleft()
print(queue)

#list del
list = [1 ,2, 3, 4, 5]
del list[0]
print(list)
del list[0:2]
print(list)
del list[:]
print(list)

#SETS
sets = set()
print(sets)
sets.add(1)
sets.add(1)
sets.add(2)
print(sets)
import random
sets.clear()
while len(sets) < 6:
    sets.add(random.randint(1,49))
print(sets)

#dictionaries
dicti = dict()
dicti[0] = "Zero"
dicti[-2] = "-Two"
dicti["ooo"] = "aaa"
print(dicti)
print("LEN:", len(dicti))
print("Value:", dicti[0])
print("Value:", dicti["ooo"])
#print("Value:", dicti["aaa"])
print("Value:", dicti.get("aaa"))
print("Value:", dicti.get("ooo"))
print("KEYS:", dicti.keys())
print("VALUES:", dicti.values())
print("ITEMS:", dicti.items())
dicti.clear()
print(dicti)