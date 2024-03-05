a = int(input("Введите число a, где a < b:"))
b = int(input("Введите число b, где b > a:"))
if a > b:
    print("a должно быть меньше b!")
for a in range(a, b + 1):
    if a % 3 == 0 and a % 5 == 0 :
        print("FizzBuzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)
