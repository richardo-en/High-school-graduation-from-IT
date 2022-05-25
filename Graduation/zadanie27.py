list = []

pocet = int(input("Koľko žiakov je v triede?\n"))
for i in range(1 ,pocet+1):
    vyska = int(input(f"Aká je výška {i}. žiaka?\n"))
    list.append(vyska)
sorted_list = sorted(list , reverse = True)
print("\n")
print(*sorted_list , sep= " , ")