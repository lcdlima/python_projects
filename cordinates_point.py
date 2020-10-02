# Read 2 values with one decimal place (x and y), which must represent the coordinates of a point on a plane. Next, determine which quadrant the point belongs to, or whether it is on one of the Cartesian axes or at the origin (x = y = 0).

ENTRADA = input()

LISTA = ENTRADA.split()

X = float(LISTA [0])
Y = float(LISTA [1])

if X == 0 and Y == 0:
    print ('Origem')
elif X == 0 and Y != 0:
    print ('Eixo Y')
elif X != 0 and Y == 0:
    print ('Eixo X')
elif X >0 and Y > 0:
    print ('Q1')
elif X < 0 and Y > 0:
    print ('Q2')
elif X < 0 and Y < 0:
    print ('Q3')
else:
    print ('Q4')