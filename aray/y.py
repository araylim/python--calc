a = int(input("malumotni kirting :" ))
d1 = { 'd2' :{
         "A1":"aray",
         "B1" :"nuritdinova",
         "kartta_raqam1": 8600} ,
      'd3':{
          "A2": "madina" ,
          "B2": "asadova",
         "kartta_raqam2" :8700 },
      'd4' :{
          "A3":"svetlana",
          "B3" :"[asanova",
          "kartta_raqam3" :8800
      }
}
if a == 1 :
    print(d1["d2"])
elif a ==  2:
    print(d1['d3'])
elif a ==3 :
    print(d1['d4'])
else:
    for x in range (15):
     print(x)