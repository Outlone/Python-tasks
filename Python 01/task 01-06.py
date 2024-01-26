print("Пожалуйста, отвечайте на вопросы строго да или нет.")
question1 = "Вопрос 1: Вы владеете навыками программирования?"
question2 = "Вопрос 2: Вы любите игры?"
print(question1)
answer1 = input()
print(question2)
answer2 = input()
if answer1 == "да" and answer2 == "да":
    print("Попробуйте себя в разработке игр.")
elif answer1 == "да" and answer2 == "нет":
    print("Попробуйте стать белым хакером.")
elif answer1 == "нет" and answer2 == "да":
    print("Можете попробовать стать тестером.")
elif answer1 == "нет" and answer2 == "нет":
    print("Очень жаль, вы нам не подходите.")
else:
    print("ОШИБКА! (Отвечайте только да или нет.)
