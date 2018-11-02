import random
arr = random.sample(range(1, 100), 10)
print(arr)

for i in range(len(arr)):
    j = i - 1
    temp = arr[i]
    while j >= 0 and temp < arr[j]:
        arr[j + 1] = arr[j]
        arr[j] = temp
        j -= 1
print(arr)