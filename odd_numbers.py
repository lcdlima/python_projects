# Read an integer value X (1 <= X <= 1000). Then show the odd numbers from 1 to X, one value per line, including X, if applicable.

N = int(input())
i = 1

if N % 2 != 0:
    while i <=N:
        print (i)
        i += 2
elif N % 2 == 0:
    N -= 1
    while i <=N:
        print (i)
        i += 2