pokracovanie="ano"
while pokracovanie == "ano":
	a = int (input ("Zadaj číslo: ")) #zadaj počet riadkov
	hviezdy = "" #definovanie prázdnej premennej
	for riadky in range (a) :
		hviezdy += "*" #hviezdy = hviezdy + "*"
		print (hviezdy)
	pokracovanie = input("Pre pokračovanie napíš ano, pre koniec Lubovoľný kláves: ")