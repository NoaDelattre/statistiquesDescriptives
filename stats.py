from math import*

total = 0

for i in range(31):
    t = float(input("Entrer une température : "))
    total = total + t
moyenne = total/(i+1)
print(moyenne)