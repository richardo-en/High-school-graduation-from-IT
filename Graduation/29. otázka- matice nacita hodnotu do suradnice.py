mat=""
rozmer=int(input('Zadaj rozmer matice: '))
for i in range(rozmer):
    pom=""
    for j in range(rozmer):
        
        x=input('Zadaj ciselnu hodnotu do suradnice => ['+str(i)+','+str(j)+'] :')
        pom = pom + x + ""
    mat += pom
    mat += "\n"
    print()
    print (mat)









  
