print ("Перед вами находится несколько дверей: 1, 2, 3. В какую вы пойдёте?")
choice = input()
if choice == "1":
    print ("Перед вами появилась ещё одна развилка из двух дверей: 1, 2. В какую вы пойдёте?")
    choice1 = input()
    if choice1 == "1":
        print ("Вы моментально упали в пропасть и умерли.")
    elif choice1 == "2":
        print ("Вам удалось выбраться из странного помещения и стать свободным.")
    else:
        print ("ОШИБКА! (Некоректное действие).")
elif choice == "2":
	print ("Вы попадаете в комнату с кучей монстров и умираете от их рук.")
elif choice == "3":
	print ("Вас сразу же проткнуло копьё-ловушка.")
else:
	print ("ОШИБКА! (Некоректное действие).")