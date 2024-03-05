coins = int(input('Coins:'))
while coins // 8 > 0:
    coins //= 8
print(coins)
