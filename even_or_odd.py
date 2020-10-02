# Read an integer N. This value will be the number of values that will be read next. For each value read, show a message in English saying if this value read is even (EVEN), odd (ODD), positive (POSITIVE) or negative (NEGATIVE). In case the value is equal to zero (0), although the correct description is (EVEN NULL), because by definition zero is even, your program should print only NULL.

N = int(input())
i = 1

while i<= N:
  num = int(input())
  i += 1
  if num %2 == 0:
    if num < 0:
      print ('EVEN NEGATIVE')
    elif num > 0: 
      print ('EVEN POSITIVE')
    else:
      print ('NULL')
  else: 
    if num < 0:
      print ('ODD NEGATIVE')
    else: 
      print ('ODD POSITIVE')