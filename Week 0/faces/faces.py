def main():
    text = input("Insert text plus emoticon to be converted: ")
    convert(text)

def convert(text):
    print(text.replace(":)", "🙂").replace(":(", "🙁"))

main()
