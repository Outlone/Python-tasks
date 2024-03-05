pir = int(input('Введите высоту пирамиды:'))
for a in range(1, pir + 1, 1):
    print(' ' * (pir - a), '*' * (2 * a - 1))
