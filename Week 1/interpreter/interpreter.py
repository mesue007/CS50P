expression = input("Expression: ")
x, y, z = expression.split(" ")
a = int(x)
b = int(z)

if y == "+":
    print(float(a+b))

elif y == "-":
    print(float(a-b))

elif y == "*":
    print(float(a*b))

elif y == "/":
    print(float(a/b))
