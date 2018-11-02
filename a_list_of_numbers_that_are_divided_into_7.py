import random
li = []
for i in range(1500, 3001):
    if i % 7 == 0 and i % 3 == 1:
        li.append(i)
print(li)
