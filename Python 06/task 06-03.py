M = int(input("Введите кол-во изучающих англ.:"))
N = int(input("Введите кол-во изучающих нем.:"))
eng = set()
germ = set()
for i in range(M):
    student = input("Ученики изучающие анг.:")
    eng.add(student)
for i in range(N):
    student = input("Ученики изучающие нем.:")
    germ.add(student)
onelanguage = eng ^ germ
if len(onelanguage):
    print(len(onelanguage))
else:
    print('NO')
