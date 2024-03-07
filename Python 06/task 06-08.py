n = int(input("Введите кол-во мужчин сотрудников в организации:"))
surname = set()
double = set()
k = 0
for i in range(n):
    name = input()
    if name not in surname:
        surname.add(name)
    else:
        k += 1
        if name not in double:
            double.add(name)
k += len(double)
print(k)
