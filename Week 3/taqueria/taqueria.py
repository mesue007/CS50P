d = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total = 0
while True:
    try:
        item = input("Item: ").lower()
        for key in d:
            if key == item:
                total = float(d[item]) + float(total)
                print(f"Total: ${total:.2f}")

    except EOFError:
        print()
        break
    except KeyError:
        pass
