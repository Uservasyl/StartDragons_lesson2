import random
#arr = random.sample(range(1, 100), 10)

arr = [4, 3, 7, 4, 3, 4, 2, 7, 5, 4, 5, 7]
print(arr)
for i in range(len(arr)):
    j = i - 1
    temp = arr[i]
    while j >= 0 and arr.count(temp) > arr.count(arr[j]):
        arr[j + 1] = arr[j]
        arr[j] = temp
        j -= 1
print(arr)

