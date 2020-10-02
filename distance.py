# Two cars (X and Y) leave in the same direction. Car X leaves at a constant speed of 60 km / h and car Y leaves at a constant speed of 90 km / h.
# In one hour (60 minutes), car Y is able to distance itself 30 kilometers from car X, that is, it is able to move one kilometer away every 2 minutes.
# Read the distance (in Km) and calculate how long it takes (in minutes) for car Y to take that distance from the other car.

distancia = int(input())

tempo = int ((distancia/30)*60)

print ('{} minutos'.format(tempo))