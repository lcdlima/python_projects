# Make a program that reads three values and displays the largest of the three values read in a row

lista_1 = input()

produto_1 = lista_1 . split ()

A = int (produto_1 [0])

B = int (produto_1 [1])

C = float (produto_1 [2])

MAIORAB = int((A+B+abs(A-B))/2)

MAIOR = int((MAIORAB+C+abs(MAIORAB-C))/2)

print ('{} eh o maior'.format(MAIOR))