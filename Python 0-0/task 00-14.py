import random
planets = ['Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун']
planet = random.choice(planets)
print('Какую планету я загадал?')
answer = input()
while answer != planet:
 if answer != planet:
  print("Загадали другую планету!")
 answer = input()
if answer == 'Плутон':
 print('Плутон уже не считается планетой.')
elif answer not in planets:
 print('Да это же вообще не название планеты Солнечной системы.')
elif answer == planet:
 print('*** Верно! *** Это', answer)
else:
 print('Неверно!')
input()
