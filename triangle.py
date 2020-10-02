# Read 3 real values (A, B and C) and check whether they form a triangle or not. If so, calculate the triangle's perimeter and display the message:
#   Perimeter = XX.X
# If not, calculate the area of the trapezoid that has A and B as the base and C as the height, showing the message
#   Area = XX.X

ENTRADA = input()

LISTA = ENTRADA . split()

A = float(LISTA[0])
B = float(LISTA[1])
C = float(LISTA[2])

if abs(B - C) < A and A < B + C and abs(A - C) < B and B < A + C and abs(A - B) < C and C < A + B:
    PERIMETRO = A + B + C
    print ('Perimetro = {:.1f}'.format (PERIMETRO))
else:
    AREA = ((A + B) * C)/2
    print ('Area = {}'. format (AREA))