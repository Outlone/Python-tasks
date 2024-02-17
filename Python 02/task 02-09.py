B = int(input("Рост Бори:"))
V = int(input("Рост Вовы:"))
D = int(input("Рост Димы:"))

if (B > V) and (B > D) and (V > D):
    print(B, V, D)
elif (B > V) and (B > D) and (V < D):
    print(B, D, V)
elif (V > B) and (V > D) and (B > D):
    print(V, B, D)
elif (V > B) and (V > D) and (B < D):
    print(V, D, B)
elif (D > B) and (D > V) and (V > B):
    print(Dima, Vova, Borya)
elif (D > B) and (D > V) and (V < B):
    print(D, B, V)
else:
    print(error)
