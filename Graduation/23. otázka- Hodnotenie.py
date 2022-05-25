
a = int(input("Zadaj plny pocet zadanych otazok na vypracovanie: "))
b = int(input("Zadaj kolko bolo vypracovanych otazok: "))
if a < b:
    print ("\n\t!!!Zle zadane hodnoty!!!")
    exit
c = (b/a)*100

if c >= 90:
     print ("\n\tDostal si 1!")
if c < 90 and c >= 80:
    print("\n\tDostal si 2!")
if c < 80 and c >= 70:
    print("\n\tDostal si 3!")
if c < 70 and c >= 60:
     print("\n\tDostal si 4!")
if c < 60:
    print("\n\tDostal si 5!")