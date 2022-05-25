# vstup
cislo = str(input("zadaj binarne cislo.. \n"))

# výstup
dlzka = len(cislo)
vysledok = 0
for c in cislo:
   # print ("c= ",c)
    dlzka -= 1
    pom = int(c)*pow(2, dlzka)
   # print ("pom= ",pom)
   # print ("dlzka=", dlzka)
    vysledok += pom
   # print ("vysledok= ", vysledok)
print("v desiatkovej je to cislo: ", vysledok)
