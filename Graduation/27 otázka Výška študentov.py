POCET = int(input("zadaj počet žiakov:"))
"""
pole = [0] * POCET
print (pole)
for i in range(POCET):
    vyska = int(input("Zadaj výšku žiaka: "))

    j = 0
    while vyska > pole[j] and j < i: # najdenie prvku v poli, kde sa vlozi vyska
        j += 1

    while j <= i: #posun ostatnych prvkov doprava
        pom = pole[j]
        pole[j] = vyska
        vyska = pom
        j += 1

for x in pole:
    print(x)
"""
list_ziaci = []
for z in range(POCET):
    list_ziaci.append("Ziak "+str(z+1)+"=")
    list_ziaci.extend([input("Zadaj vysku ziaka: ")])
print(*list_ziaci)
sort_list_ziaci=sorted(list_ziaci, reverse=True)
print(*sort_list_ziaci)
