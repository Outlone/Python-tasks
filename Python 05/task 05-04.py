n = int(input("Введите кол-во строк:"))
i = False
for a in range(n):
    words = input("Введите предложения:")
    if 'кот' in words or 'Кот' in words:
        a = True
        break
if a:
    print('МЯУ')
else:
    print('НЕТ')
