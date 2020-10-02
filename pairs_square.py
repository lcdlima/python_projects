# Read an integer value N. Display the square of each of the even values, from 1 to N, including N, if applicable.

N = int(input())
i = 2

if N % 2 == 0:
    while i <= N:
        pot = i**2
        print (('{}^2 = {}'). format (i, pot) )
        i += 2
else: 
    while i < N:
        pot = i**2
        print (('{}^2 = {}'). format (i, pot) )
        i += 2

