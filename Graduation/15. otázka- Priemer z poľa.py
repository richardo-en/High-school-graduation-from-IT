# vstup načíta čísla do pola

list = []

while True:
    try:
        x = float(input("x:"))
        list.append(x)
    except:
            break
print (list)

#prg na priemer


sucet = 0
for i in range(len(list)):
    sucet = sucet +list[i]

vysledok = sucet/(len(list))

# výsledok zaokrúhlení na 2 des. miesta
print(round(vysledok,2))
