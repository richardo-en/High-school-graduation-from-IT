# vkladanie čísiel do poľa
#hľadá MAX číslo

pole = []
while True:
    try:
        if True:
            x = int(input("x: "))
            pole.append(x)
    except:
            break
#print (pole)

# študuj.it         
maximum = -100

for i in range(len(pole)):
    if pole[i]>maximum:
        maximum = pole[i]
        

# alebo použi naprog. funkciu

print (max(pole))
