#Napíšte program, ktorý vypíše súčet všetkých čísel nachádzajúcich sa v zadanom intervale.
minimum = int(input("Zadaj min:"))
maximum = int(input("Zadaj max:"))

#pri zlom zadani cisel nastane vymena
if  maximum<minimum:
    mid=minimum
    minimum=maximum
    maximum=mid

ans=0

while minimum <= maximum:
    ans += minimum
    minimum += 1
print(ans)

    
    
