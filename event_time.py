# Pedrinho is organizing an event at his University. The event should take place in April, starting and ending within the month. The problem is that Pedrinho wants to calculate how long the event will last, since he knows when it starts and when the event ends.
# Knowing that the event can last from a few seconds to several days, you should help Pedrinho to calculate the duration of this event.

A1 = str(input()).split()
DI = int(A1[1])
A2 = str(input()).split(' : ')
HI = int(A2[0])
MI = int(A2[1])
SI = int(A2[2])

B1 = str(input()).split()
DF = int(B1[1])
B2 = str(input()).split(' : ')
HF = int(B2[0])
MF = int(B2[1])
SF = int(B2[2])

TI = HI*3600 + MI*60 + SI
TF = HF*3600 + MF*60 + SF

if TI < TF:
  DIAS = DF - DI
  HORAS = (TF - TI)//3600
  M = (TF - TI)%3600
  MINUTOS = M//60
  SEGUNDOS = M%60
  print ('{} dia(s)'.format(DIAS))
  print ('{} hora(s)'.format(HORAS))
  print ('{} minuto(s)'.format(MINUTOS))
  print ('{} segundo(s)'.format(SEGUNDOS))
elif TI > TF:
  DIAS = DF - DI -1
  HORAS = (86400 - TI + TF)//3600 
  M = (86400 - TI + TF)%3600
  MINUTOS = (M)//60
  SEGUNDOS = (M)%60
  print ('{} dia(s)'.format(DIAS))
  print ('{} hora(s)'.format(HORAS))
  print ('{} minuto(s)'.format(MINUTOS))
  print ('{} segundo(s)'.format(SEGUNDOS))
elif TI == TF:
  print ('{} dia(s)'.format(DF-DI))
  print ('24 hora(s)')
  print ('0 minuto(s)')
  print ('0 segundo(s)')