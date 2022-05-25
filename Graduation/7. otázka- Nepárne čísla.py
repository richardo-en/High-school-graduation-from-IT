a = int(input())
b = int(input())

pom = 0
vypis = ""
while a<=b:
    if(a%2==1):
        if(pom<5):
            vypis+=str(a)+" "
            pom+=1
            a+=1
        else:
            vypis += "\n"+str(a)+" "
            pom = 1
            a += 1
    else: a = a + 1 
        
print(vypis)
