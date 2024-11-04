cCase = input("camelCase: ")

for c in cCase:
    if c.isupper() == False:
        print(c, end="")
    elif c.isupper() == True:
        print(f"_{c.lower()}", end="")

print()
