# Read 4 integer values A, B, C and D. Next, if B is greater than C and if D is greater than A, and the sum of C with D is greater than the sum of A and B and if C and D, both are positive and if variable A is to write the message "Values accepted", otherwise write "Values not accepted".

VALORES = input()

LISTA = VALORES.split()

A = int(LISTA[0])
B = int(LISTA[1])
C = int(LISTA[2])
D = int(LISTA[3])

if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A%2 ==0: 
    print ('Valores aceitos')
   
else:
    print ('Valores nao aceitos')