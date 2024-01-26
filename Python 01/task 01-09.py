print("Регистрация резервной почты.")
login = "Введите логин:"
rezerv_email = "Введите резервную почту:"
print(login)
answer1 = input()
print(rezerv_email)
answer2 = input()
if "@" in answer1 and "@" in answer2:
    print("Некорректный логин")
elif not "@" in answer1 and not "@" in answer2 :
    print("Некорректный адрес")
elif not "@" in answer1 and "@" in answer2:
    print("OK")
elif "@" in answer1 and not "@" in answer2:
    print("Абсолютно неправильно!")
