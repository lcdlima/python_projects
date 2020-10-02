# Read an integer value, which is the duration in seconds of a given event in a factory, and enter it in the format hours: minutes: seconds.

N = int(input())

HORAS = int(N//3600)
N = N%3600

MINUTOS = int(N//60)
N = N%60

SEGUNDOS = N

print ('{}:{}:{}'.format (HORAS,MINUTOS,SEGUNDOS))