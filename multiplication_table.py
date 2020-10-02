# Read 1 integer value N (2 <N <1000). Next, show the N times table:
# 1 x N = N 2 x N = 2N ... 10 x N = 10N

N = int(input())

for i in range(1,11):
  print ('{} x {} ='.format(i,N), i*N)
  i +=1