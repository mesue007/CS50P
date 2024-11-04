import inflect
p = inflect.engine()
i = 0
while True:
    try:
        person = input("Name: ")
        if i > 0:
            persons = (persons + " " + person)
        else:
            persons = person
        i += 1


    except EOFError:
        try:
            persons = persons.split()
            print(f"Adieu, adieu, to {p.join(persons)}")
            break
        except NameError:
            break
    except KeyError:
        pass
