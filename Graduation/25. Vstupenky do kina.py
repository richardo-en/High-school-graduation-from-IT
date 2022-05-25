#Program na vetvenie - listky do kina

start=True
while start:
    
    vek=int(input('Zadajte vek: '))

    if vek<=6:
        print('Vstupenka zdarma!')
    elif vek>6 and vek<=15:
         print('Vstupenka: 5€')
    elif vek>15 and vek<=61:
        print('Vstupenka: 7€')
    elif vek>61:
        print('Vstupenka: 2€')
    