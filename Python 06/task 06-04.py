M = int(input("Введите кол-во изучающих англ.:"))
N = int(input("Введите кол-во,  изучающих нем.:"))
eng = set()
germ = set()
for i in range(M + N):
    students = input()
    if i < M:
        eng.add(students)
    else:
        ger.add(students)
onelanguage = eng ^ ger
if len(onelanguage):
    print(len(onelanguage))
else:
    print('NO')
