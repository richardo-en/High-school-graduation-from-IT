a = int (input ("prve cislo: "))
x = input ("matematicka operacia + - * / ")
b = int (input ("druhe cislo: "))         


if x in "+-*/" :
    if x == "+" :
        ans = a + b
        print ("vysledok je", ans)
    elif x == "-" :
        ans = a - b
        print ("vysledok je", ans)
    elif x == "*" :
        ans = a * b
        print ("vysledok je", ans)
    elif x == "/" :
        ans = a / b
        print ("vysledok je", ans)
else :
    print ("Zlý operátor!")
