# Make a program that reads 5 integer values. Count how many of these entered values are even and show this information.

i = 1
SOMA = 0

while i <= 5:
    N = int(input())
    i += 1
    if N%2 == 0:
        SOMA += 1

print ('{} valores pares'.format (SOMA))