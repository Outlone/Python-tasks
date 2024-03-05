count = 0
a = int(input())
for b in range(1, a + 1):
    if a % b == 0:
        if b != a:
            print(str(i), end=" ")
        if b == a:
            print(str(i))
        count += 1
if a == 1:
    print("НЕТ")
elif count == 2:
    print("ПРОСТОЕ")
else:
    print("НЕТ")
