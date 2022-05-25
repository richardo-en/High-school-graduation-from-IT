# vstup nejaké kladné číslo aspoň 10+
# použi napr.: 7 alebo 27

n = int(input("načítaj n...: "))
kroky = 0

while n != 1:
    if n % 2 == 0:
        n = int(n /2)
        print (n)
        kroky += 1
    else:
        n = (n * 3)+1
        print (n)
        kroky += 1
print(kroky)

