import random
# генерація списку Фібоначчі.
n = int(input("Введіть довжину списку: \n"))
a = 0
b = 1
li = []
N = n * 5
while len(li) < N:
    c = a + b
    a = b
    b = c
    li.append(c)
print(li)

# генерація списку довжиною n із списку Фібоначчі.
arr = random.sample(li, n)


# сортування методом включення
for i in range(len(arr)):
    j = i - 1
    temp = arr[i]
    while j >= 0 and temp < arr[j]:
        arr[j + 1] = arr[j]
        arr[j] = temp
        j -= 1
print(arr)