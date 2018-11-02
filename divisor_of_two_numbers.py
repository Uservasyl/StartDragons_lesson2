a = int(input("Введіть перше число: \n"))
b = int(input("Введіть друге число: \n"))

i = 1
li = []
while i <= a and i <= b:
    if a % 2 == 0 and b % 2 == 0:
        li.append(i)
    i += 1
print("Найбільший спільний дільник - це {}".format(li[-1]))
