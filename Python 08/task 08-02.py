word1 = input("Введите первое слово:")
word2 = input("Введите сторое слово: ")
bull = 0
cow = 0
for i in set(word1) & set(word2):
    if word1.index(i) == word2.index(i):
        bull += 1
    else:
        cow += 1
print(bull, cow)
