import random
arr = random.sample(range(1, 100), 10)

for i in range(len(arr)):
    j = i - 1
    temp = arr[i]
    while j >= 0 and temp < arr[j]:
        arr[j + 1] = arr[j]
        arr[j] = temp
        j -= 1
print(arr)
i = 1
L = 0
R = len(arr)
x = int(input("Введіть число для пошуку:\n"))
Ns = L + (R - L) // 2
while i <= len(arr):
    if x < arr[Ns]:
        R = Ns
    elif x > arr[Ns]:
        L = Ns + 1
    elif x == arr[Ns]:
        print("Число є в списку!")
        break
    Ns = L + (R - L) // 2
    i += 1
else:
    print("Числа немає в списку.")