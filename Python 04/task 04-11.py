ave = 0
sum = 0
n = int(input('Введите кол-во тестируемых людей:'))
for a in range(n):
    iq = int(input('Введите iq:'))
    sum += iq
    ave = sum/(a+1)
    if iq == ave:
        print('0')
    elif iq > ave:
        print('>')
    else:
        print('<')
