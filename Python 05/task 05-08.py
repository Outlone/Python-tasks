word = ''
n = 0
cat = -1
num = 1
while word != 'Стоп':
    word = input("Введите текст:")
    if 'Кот' in word or 'кот' in word:
        n += 1
    if ('Кот' in word or 'кот' in word) and cat == -1:
        cat = num
    num += 1
print(n, cat)
