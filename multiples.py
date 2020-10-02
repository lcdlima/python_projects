# Read 2 integer values (A and B). Afterwards, the program should show a message "Are Multiples" or "Not Multiples", indicating if the values read are multiple with each other.

ENTRADA = input()

LISTA = ENTRADA.split()

A = int(LISTA[0])
B = int(LISTA[1])

if A > B: 
    DIV = A%B
else:
    DIV = B%A
    
if DIV == 0:
    print ('Sao Multiplos')
else:
    print ('Nao sao Multiplos') 