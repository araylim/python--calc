amallar = input("Amalni kirgizing: ")
a = int(input("1 - sonni kirgizing :"))
b = int(input("2 - sonni kirgizing :"))
if amallar == "+":
    print(a + b)
elif amallar == "-" :
    print(a - b)
elif amallar == "*" :
    print(a * b) 
elif amallar == "/" :
    print(a / b)
elif amallar == "**" :
    print(a ** b)
elif amallar == "%" :
    print(a % b)
elif amallar == "!=" :
    print(a != b)
elif amallar == "//" :
    print(a // b)
elif amallar == "==" :
    print(a == b)
else:
    print("siz mavjut bo'lmagan sonni kiritigiz! ")
    