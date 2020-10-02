# Read an integer between 1 and 12, inclusive. Corresponding to this value, the month of the year must be presented in full, in English, with the first letter in uppercase.

NUMERO = [1,2,3,4,5,6,7,8,9,10,11,12]
MES = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

ENTRADA = int(input())

N = NUMERO.index(ENTRADA)

print (MES[N])