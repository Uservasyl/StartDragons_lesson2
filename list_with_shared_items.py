import random
# list_A = random.sample(range(1, 100), 10)
# list_B = random.sample(range(1, 100), 10)

list_A = [7, 77, 38, 73, 49, 32, 13, 93, 39, 48, 13, 69, 48, 95, 77, 89, 26, 20, 19, 19]
list_B = [8, 75, 8, 75, 4, 2, 13, 9, 39, 48, 13, 69, 48, 95, 71, 90, 15, 20, 17, 19]
list_C = []
i = 0
m = 1
while i < len(list_A):
    j = m
    while j < len(list_B):
        if list_A[i] == list_B[j]:
            list_C.append(list_B[j])
        j += 1
    i += 1
    m += 1
print(list_C)