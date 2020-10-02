# Read 3 floating point values and calculate the roots of the Bhaskara equation. If it is not possible to calculate the roots, display the corresponding message “Impossible to calculate”, in case there is a division by 0 or negative number root.

VALORES = input()

LISTA = VALORES. split()

A = float (LISTA [0])
B = float (LISTA [1])
C = float (LISTA [2])

DELTA = B**2 - 4*A*C

if DELTA < 0 or A == 0:
    print ('Impossivel calcular')
else:
    R1 = (-B + DELTA**(1/2))/(2*A)
    print ('R1 = {:.5f}'.format (R1))
    R2 = (-B - DELTA**(1/2))/(2*A)
    print ('R2 = {:.5f}'.format (R2))