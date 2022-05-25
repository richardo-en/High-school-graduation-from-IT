mat=""
rozmer=int(input('Zadaj rozmer matice: '))
for i in range(rozmer):
    pom=""
    for j in range(rozmer):
        ret=(i)+(j)
        x=input(ret)
        pom = pom + x + " "
    mat += pom
    mat += "\n"
    print()

print (mat)





  
