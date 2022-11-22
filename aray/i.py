a = input("Amalni kiriting :")
b =int(input("1-sonni kirining : "))
c = int(input("2-sonni kirining : "))
def cal(b,c) :
    if a == "+" :
        print(b+c)
    elif a == "-":
        print(b-c)
    elif a == "*":
        print(b*c)
    elif a == "/":
        print(b/c)
    elif a == "**":
        print(b**c)
    elif a == "%":
        print(b%c)
    elif a == "==":
        print(b==c)
    elif a == "!=":
        print(b!=c)
    elif a == "//":
        print(b//c)
    else:
        print("hatto")


cal(b,c)