a = set()
b = set()
c = input(int("Введите номера домов на первом листке:"))
while c != "":
    a.add(c)
    c = input(int("Введите номера домов на первом листке:"))
a.add(c)
d = input(int("Введите номера домов на втором листке:"))
while d != "":
    b.add(d)
    d = input(int("Введите номера домов на втором листке:"))
intersection = a & b
if not intersection:
    print("EMPTY")
else:
    for i in intersection:
        print(i)
