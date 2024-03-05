check = 0
while check == 0:
    password1 = input("Введите пароль:")
    password2 = input("Введите пароль повторно:")
    if len(password1) < 8:
        print('Короткий.')
    elif "123" in password1:
        print('Простой.')
    elif password1 != password2:
        print('Пароли различаются.')
    else:
        print('Ок')
