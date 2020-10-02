# Read 5 Integer values. Then show how many entered values were even, how many entered values were odd, how many entered values were positive and how many entered values were negative.

i = 1
PAR = 0 
IMPAR = 0
POSITIVO = 0
NEGATIVO = 0

while i <= 5:
    N = int(input())
    i += 1
    if N%2 == 0:
        PAR += 1
    elif N%2 != 0:
        IMPAR += 1
    if N > 0:
        POSITIVO += 1
    elif N < 0:
        NEGATIVO += 1

print ('{} valor(es) par(es)'.format (PAR))
print ('{} valor(es) impar(es)'.format (IMPAR))
print ('{} valor(es) positivo(s)'.format (POSITIVO))
print ('{} valor(es) negativo(s)'.format (NEGATIVO))
