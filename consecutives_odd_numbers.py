# Read 2 integer values X and Y. Next, calculate and show the sum of the odd numbers between them.

X = int(input())
Y = int(input())

i = 0
SOMA = 0

if X < Y: 
    X += 1
    LISTA = list(range(X,Y))
    for i in LISTA:
        if (i%2) != 0:
            SOMA += i

elif X > Y:
    Y += 1
    LISTA = list(range(Y,X))
    for i in LISTA:
        if (i%2) != 0:
            SOMA += i

print (int(SOMA))