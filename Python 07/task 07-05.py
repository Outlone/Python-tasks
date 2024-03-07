word1 = str(input("Введите первое слово:"))
word2 = str(input("Введите второе слово:"))
while word1[-1] == word2[0]:
    word = str(input("Введите слово :"))
    if word[-1] == word2[0]:
        word2 = str(input("Введите новое слово :"))
    else:
        print(word)
        break
