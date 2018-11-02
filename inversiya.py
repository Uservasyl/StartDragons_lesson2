import random
arr = random.sample(range(1, 100), 10)
print(arr)
i = 0
for j in range(len(arr) - 1):
    if arr[j] > arr[j+1]:
        i += 1
print("Кількість інверсій рівна - {}".format(i))