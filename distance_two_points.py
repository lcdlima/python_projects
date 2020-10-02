# Read the four values corresponding to the x and y axes of any two points in the plane, p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing 4 decimal places after the comma.

P1 = str(input())

P1 = P1.split()

x1 = float(P1[0])

y1 = float(P1[1])

P2 = str(input())

P2 = P2.split()

x2 = float(P2[0])

y2 = float(P2[1])

distancia = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print ('{:.4f}'.format (distancia))