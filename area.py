# Write a program that reads three double-precision floating point values: A, B and C. Then, calculate and show:
# a) the area of the right triangle with A as the base and C as the height.
# b) the area of the circle of radius C. (pi = 3.14159)
# c) the area of the trapezoid that has A and B for bases and C for height.
# d) the area of the square with side B.
# e) the area of the rectangle that has sides A and B.

lista_1 = input()

produto_1 = lista_1 . split ()

A = float (produto_1 [0])

B = float (produto_1 [1])

C = float (produto_1 [2])

print ('TRIANGULO: {:.3f}'. format ((A*C)/2))

print ('CIRCULO: {:.3f}'. format (3.14159 * C**2))

print ('TRAPEZIO: {:.3f}'. format ((A+B)*C/2))

print ('QUADRADO: {:.3f}'. format (B**2))

print ('RETANGULO: {:.3f}'. format (A*B))