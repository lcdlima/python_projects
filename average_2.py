# Read 3 values, in this case, variables A, B and C, which are the three grades of a student. Next, calculate the student's average, knowing that grade A has weight 2, grade B has weight 3 and grade C has weight 5. Consider that each grade can range from 0 to 10.0, always to one decimal place.

A = float (input ())

B = float (input ())

C = float (input ())

MEDIA = (A*2 + B*3 + C*5) / 10

print ('MEDIA = {:.1f}'.format (MEDIA))