pass1 = input("Введите пароль:")
pass2 = input("Введите пароль повторно для подтверждения:")
while pass1 == pass2 and len(pass1) < 8:
    print("Короткий.")
    pass1 = input("Введите пароль:")
    pass2 = input("Введите пароль повторно для подтверждения:")
    while pass1 != pass2 and len(pass1) >= 8:
        print("Пароли не совпадают.")
        pass1 = input("Введите пароль:")
        pass2 = input("Введите пароль повторно для подтверждения:")
while pass1 != pass2 and len(pass1):
    print("Пароли не совпадают.")
    pass1 = input("Введите пароль:")
    pass2 = input("Введите пароль повторно для подтверждения:")
    while pass1 == pass2 and len(pass1) < 8:
        print("Короткий.")
        pass1 = input("Введите пароль:")
        pass2 = input("Введите пароль повторно для подтверждения:")
if pass1 == pass2 and len(pass1) >= 8:
    print("Вход разрешён.")
