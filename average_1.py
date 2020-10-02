# Read 2 double-precision floating point values A and B, which correspond to 2 grades of a student. Next, calculate the student's average, knowing that grade A has a weight of 3.5 and grade B has a weight of 7.5 (The sum of the weights is therefore 11). Assume that each note can go from 0 to 10.0, always with one decimal place.

A = float (input())

B = float (input())

MEDIA = (A*3.5+B*7.5)/11

print ('MEDIA = {:.2f}'.format(MEDIA))