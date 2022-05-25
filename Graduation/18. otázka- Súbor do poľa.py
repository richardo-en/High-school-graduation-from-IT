start = True

while start:
    
    subor = input("zadaj názov súboru:")
    if subor == "end":
        quit()
    file = open(subor)

    pole = []
    # output

    for line in file:
        pole.append(int(line))
    if(len(pole)==0):
        print("None")
    else:
        print(pole)
        spolu = 0
        for i in range(len(pole)):
            spolu += pole[i]
            print(spolu)

        priemer = 0
        priemer = spolu / len(pole)
    print("Priemerná hodnota je: ", priemer)