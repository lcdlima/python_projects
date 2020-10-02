# In this problem, you should read the code of a part 1, the number of parts 1, the unit value of each part 1, the code of a part 2, the number of parts 2 and the unit value of each part 2. After , calculate and show the amount to be paid.

lista_1 = input()

produto_1 = lista_1 . split ()

codigo_1 = int (produto_1 [0])

numero_1 = int (produto_1 [1])

valor_1 = float (produto_1 [2])

lista_2 = input()

produto_2 = lista_2 . split ()

codigo_2 = int (produto_2 [0])

numero_2 = int (produto_2 [1])

valor_2 = float (produto_2 [2])

total = numero_1*valor_1 + numero_2*valor_2

print ('VALOR A PAGAR: R$ {:.2f}'.format (total)) 