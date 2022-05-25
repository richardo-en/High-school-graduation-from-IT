n = int(input())
m = int(input())

# výstup
for i in range(n):
    riadok = ""
    for j in range(m):
        if(i%2==0 and j%2==0):
            riadok += "x"
        elif(i%2==0 and j%2==1):
            riadok += "o"
        elif(i%2==1 and j%2==0):
            riadok += "o"
        else:
            riadok += "x"
    print(riadok)