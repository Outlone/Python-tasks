n = int(input("Введите кол-во покупок:"))
list = []
for i in range(n):
    word = input("Введите название товара:")
    list.append(word)
for word in list:
    print(word)
