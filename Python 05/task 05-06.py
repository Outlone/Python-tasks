sum = 0
a = int(input("Введите числа:"))
count = 0
while a != 0:
    sum += a
    if sum == 10:
        print(count)
        break
    count += 1
    a = int(input("Введите числа:"))
