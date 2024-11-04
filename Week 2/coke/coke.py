coin = int(input("Insert Coin: "))

i = 50

while i - coin > 0:
    if coin == 25:
        print(f"Amount Due: {i - 25}")
    elif coin == 10:
        print(f"Amount Due: {i - 10}")
    elif coin == 5:
        print(f"Amount Due: {i - 5}")
    else:
        print(f"Amount Due: {i}")
    i = i - coin
    coin = int(input("Insert Coin: "))

if i - coin == 0:
    print("Change Owed: 0")
elif i - coin < 0:
    print(f"Change Owed: {coin-i}")
