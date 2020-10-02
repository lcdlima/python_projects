# Read an integer value N. Display all numbers between 1 and 10000 that divided by N give remainder equal to 2.

N = int(input())
i = 0

for i in range(0,10000):
  if i % N == 2:
    print (i)
  i += 1