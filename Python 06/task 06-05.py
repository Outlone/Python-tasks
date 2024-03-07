M = int(input("Введите кол-во изучающих англ.:"))
N = int(input("Введите кол-во изучающих нем.:"))
K = int(input("Введите кол-во изучающих франц.:"))
first = set()
second = set()
for i in range(M + N + K):
    student = input()
    if student not in first:
        first.add(student)
    elif student not in second:
        second.add(student)
    else:
        second.remove(student)
if len(second):
    print(len(second))
else:
    print('NO')
