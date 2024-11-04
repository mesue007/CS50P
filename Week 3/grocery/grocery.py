i = 0
while True:
    try:
        item = input().upper()
        if i > 0:
            items.append(item)
        else:
            items = [item]
        i += 1


    except EOFError:
        try:
            print()
            items = sorted(items)
            d = dict((x,items.count(x)) for x in set(items))
            for key, value in d.items():
                print(f"{value} {key}")
            break
        except NameError:
            break
    except KeyError:
        pass
