#!/usr/bin/python3
import random
arr = random.sample(range(1, 100), 10)
print(arr)
i = 0
while i < len(arr):
    for j in range(len(arr)-1):
        if arr[j] % 2 == 0 and arr[j+1] % 2 == 0:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        elif arr[j] % 2 == 1 and arr[j+1] % 2 == 0:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        elif arr[j] % 2 == 1 and arr[j+1] % 2 == 1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    i += 1
print(arr)
