# Read an integer value X. Then display the 6 consecutive odd values starting from X, one value per line, including X if applicable.

N = int(input())
i = 1

if N%2 != 0:
    while i <= 6:
        print (N)
        i += 1
        N += 2
elif N%2 == 0:
    N += 1
    while i <= 6:
        print (N)
        i += 1
        N += 2