from math import*

t = [1, 5, 2, 9, 4, -3]
minimal = t[0]
maximal = t[0]

for i in range(len(t)):
    if minimal > t[i]:
        minimal = t[i]
    elif maximal < t[i]:
        maximal = t[i]
    i = i+1
print(minimal)
print(maximal)

def etendue(minimal, maximal):
    resultat = maximal-minimal
    return resultat

print(etendue(minimal, maximal))
print(etendue(5, 8))