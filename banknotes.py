# Read an integer value. Next, calculate the smallest possible number of notes (banknotes) into which the value can be broken down. The notes considered are 100, 50, 20, 10, 5, 2 and 1. Next, show the value read and the list of necessary notes.

N = int(input())

print (N)

N100 = int (N//100)
print ('{} nota(s) de R$100,00'.format (N100))
VALOR = N%100

N50 = int (VALOR//50)
print ('{} nota(s) de R$50,00'.format (N50))
VALOR = VALOR%50

N20 = int (VALOR//20)
print ('{} nota(s) de R$20,00'.format (N20))
VALOR = VALOR%20

N10 = int (VALOR//10)
print ('{} nota(s) de R$10,00'.format (N10))
VALOR = VALOR%10

N5 = int (VALOR//5)
print ('{} nota(s) de R$5,00'.format (N5))
VALOR = VALOR%5

N2 = int (VALOR//2)
print ('{} nota(s) de R$2,00'.format (N2))
VALOR = VALOR%2

N1 = int (VALOR)
print ('{} nota(s) de R$1,00'.format (N1))