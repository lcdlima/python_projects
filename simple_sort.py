# Read 3 whole values and sort them in ascending order. At the end, show the values in ascending order, a blank line and then the values in the sequence as they were read.

ENTRADA = input()

LISTA = ENTRADA . split()

A = int (LISTA [0])
B = int (LISTA [1])
C = int (LISTA [2])

if A < B and A < C:
  print (A)
  if B < C:
    print (B)
    print (C)
  else:
    print (C)
    print (B)

if B < A and B < C:
  print (B)
  if A < C:
    print (A)
    print (C)
  else:
    print (C)
    print (A)

if C < A and C < B:
  print (C)
  if A < B:
    print (A)
    print (B)
  else:
    print (B)
    print (A)
      
print ("")
print (A)
print (B)
print (C)