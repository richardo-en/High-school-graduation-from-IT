a = int (input ("Zadaj binárny kód: "))

b = a
c = 0
d = 0
    
while(a != 0): 
    dec = a % 10
    #print("dec= ",dec)
    c = c + dec * pow(2, d)
    #print("c= ",c)
    a = a//10
    #print("a= ",a)
    d += 1
    #print("d= ",d)
print(b, "bin = ", c, " dec")
