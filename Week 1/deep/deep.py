def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    elif ignorespace(answer) == "42":
        print("Yes")
    elif answer.lower() == "forty two":
        print("Yes")
    else:
        print("No")

def ignorespace(text):
    return text.replace(" ", "")

main()
