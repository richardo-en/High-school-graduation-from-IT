# vstup
pole = []
while True:
    try:
        x = int(input("x:"))
        pole.append(x)
    except:
            break

nove_pole = []

# výstup
for i in range(len(pole)):
    if(pole[i]%2==0):
        nove_pole.append(pole[i])

print(nove_pole)
