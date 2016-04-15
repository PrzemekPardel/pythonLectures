#random
import random

#standard solution
for a in range(1,7):
    print(random.randint(1,49))

#optimal
list = []
ret = []
for a in range(1, 50):
    list.append(a)

print(list)

for a in range(1,7):
    rnd = random.choice(list)
    print("Wylosowano:", rnd)
    ret.append(rnd)
    list.remove(rnd)
    print("LISTA RND:", list)

print("Final RND list:", ret)

#extend
list2 = [100, 200]
ret.extend(list2)
print(ret)

#insert
ret.insert(1,300)
print(ret)

#remove
ret.remove(300)
print(ret)

#pop
ret.pop(0)
print(ret)

#pop
ret.pop()
print(ret)

#clear
#ret.clear()
print(ret)

#clear
ret.sort()
print(ret)