import random
# li = random.sample(range(1, 100), 10)
# print(li)
li = [7, 77, 38, 73, 49, 32, 13, 93, 39, 48, 13, 69, 48, 95, 77, 89, 26, 20, 19, 19]
# li = [4, 3, 7, 4, 3, 4, 2, 7, 5, 4, 5, 7]
print(li)
i = 0
while i < len(li):
    for j in li:
        if li.count(j) > 1:
            li.remove(j)
    i += 1
print(li)
