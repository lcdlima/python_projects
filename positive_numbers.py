# Make a program that reads 6 values. These values will only be negative or positive (disregard the null values). Next, show the number of positive values entered.

N = 1
i = 0

while N <= 6:
    ENT = float(input())
    N += 1
    if ENT > 0:
        i += 1

print ('{} valores positivos'. format (i))