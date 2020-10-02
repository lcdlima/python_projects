# Read 3 floating point values A, B and C and order them in descending order, so that side A represents the largest of the 3 sides. Next, determine the type of triangle these three sides form, based on the following cases, always writing an appropriate message:
#   if A ≥ B + C, display the message: NAO FORMMA TRIANGULO
#   if A2 = B2 + C2, present the message: TRIANGULO RECTANGULO
#   if A2> B2 + C2, present the message: TRIANGULO OBTUSANGULO
#   if A2 <B2 + C2, present the message: TRIANGULO ACUTANGULO
#   if the three sides are equal, present the message: TRIANGULO EQUILATERO
#   if only two sides are equal, present the message: TRIANGULO ISOSCELES

ENTRADA = input().split()

a = float(ENTRADA [0])
b = float(ENTRADA [1])
c = float(ENTRADA [2])

if a > b and a > c:
    A = a
    if b > c:
        B = b
        C = c
    else:
        B = c
        C = b

elif b > a and b > c:
    A = b
    if a > c:
        B = a
        C = c
    else:
        B = c
        C = a

elif c > a and c > b:
    A = c
    if a > b:
        B = a
        C = b
    else:
        B = b
        C = a
        
elif a == b:
    if b > c:
        A = a
        B = b
        C = c
    else:
        A = c
        B = a
        C = b
        
elif a == c:
    if c > b:
        A = a
        B = c
        C = b
    else:
        A = b
        B = a
        C = c

elif b == c:
    if c > a:
        A = b
        B = c
        C = a
    else:
        A = a
        B = c
        C = b

if A >= B + C:
    print ('NAO FORMA TRIANGULO')
elif A**2 == B**2 + C**2:
    print ('TRIANGULO RETANGULO')
elif A**2 > B**2 + C**2:
    print ('TRIANGULO OBTUSANGULO')
elif A**2 < B**2 + C**2:
    print ('TRIANGULO ACUTANGULO')
    
if A == B and B == C:
    print ('TRIANGULO EQUILATERO')
if (A == B and B != C) or (B == C and B != A):
    print ('TRIANGULO ISOSCELES')
