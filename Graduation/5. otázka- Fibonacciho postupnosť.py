a = int(input("Prvé číslo:\n"))
b = int(input("Druhé číslo:\n"))
c = int(input("do?\n"))

pole = [a, b]

# výstup
for i in range(c):
    pole.append(pole[-1]+pole[-2])
print(pole)
