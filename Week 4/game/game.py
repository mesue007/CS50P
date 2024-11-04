import random
def main():
    while True:
        n = input("Level: ")
        if n.isdigit() == True:
            if int(n) > 0:
                guess(n)
                break

        else:
            pass

def guess(s):
    a = random.randint(1, int(s))
    while True:
        int(a)
        g = input("Guess: ")

        if g.isdigit() == False:
            pass

        elif int(g) > int(s) or int(g) < 1:
            pass

        elif int(g) < a:
            print("Too small!")

        elif int(g) > a:
            print("Too large!")

        else:
            print("Just right!")
            break


main()
