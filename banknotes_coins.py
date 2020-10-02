# Read a floating point value to two decimal places. This value represents a monetary value. Next, calculate the smallest number of notes and coins possible into which the value can be broken down. The notes considered are 100, 50, 20, 10, 5, 2. The possible currencies are 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Then show the list of notes required.

N = float(input())
N += 0.001

print ('NOTAS:')

N100 = int (N//100)
print ('{} nota(s) de R$ 100.00'.format (N100))
VALOR = N%100

N50 = int (VALOR//50)
print ('{} nota(s) de R$ 50.00'.format (N50))
VALOR = VALOR%50

N20 = int (VALOR//20)
print ('{} nota(s) de R$ 20.00'.format (N20))
VALOR = VALOR%20

N10 = int (VALOR//10)
print ('{} nota(s) de R$ 10.00'.format (N10))
VALOR = VALOR%10

N5 = int (VALOR//5)
print ('{} nota(s) de R$ 5.00'.format (N5))
VALOR = VALOR%5

N2 = int (VALOR//2)
print ('{} nota(s) de R$ 2.00'.format (N2))
VALOR = VALOR%2

print ('MOEDAS:')

M1 = int (VALOR//1)
print ('{} moeda(s) de R$ 1.00'.format (M1))
VALOR = VALOR%1

M50 = int (VALOR//0.5)
print ('{} moeda(s) de R$ 0.50'.format (M50))
VALOR = VALOR%0.5

M25 = int (VALOR//0.25)
print ('{} moeda(s) de R$ 0.25'.format (M25))
VALOR = VALOR%0.25

M10 = int (VALOR//0.1)
print ('{} moeda(s) de R$ 0.10'.format (M10))
VALOR = VALOR%0.1

M5 = int (VALOR//0.05)
print ('{} moeda(s) de R$ 0.05'.format (M5))
VALOR = VALOR%0.05

M01 = int (VALOR//0.01)
print ('{} moeda(s) de R$ 0.01'.format (M01))