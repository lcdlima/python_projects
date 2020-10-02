# Joãozinho wants to calculate and show the amount of liters of fuel spent on a trip, when using a car that does 12 KM / L. For this, I would like you to attend to it through a simple program. To perform the calculation, the time spent on the trip (in hours) and the average speed during the trip (in km / h) must be reported. Thus, one can obtain the distance covered and calculate how many liters would be needed. Show the value to 3 decimal places after the period.

TEMPO = int(input())

VELOCIDADE = int(input())

GASTO = (TEMPO*VELOCIDADE)/12

print ('{:.3f}'.format (GASTO))