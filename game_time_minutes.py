# Read the start time, start minute, end time and end minute of a game. Then calculate the duration of the game.
# Note: The game has a minimum duration of one (1) minute and a maximum duration of 24 hours.

ENTRADA = input().split()

HI = int(ENTRADA[0])
MI = int(ENTRADA[1])
HF = int(ENTRADA[2])
MF = int(ENTRADA[3])

TI = HI*60 + MI
TF = HF*60 + MF

if TI < TF:
  HORAS = (TF - TI)//60
  MINUTOS = (TF - TI)%60
  print ('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format (HORAS, MINUTOS))
elif TI > TF:
  HORAS = (1440 - TI + TF)//60
  MINUTOS = (1440 - TI + TF)%60
  print ('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format (HORAS, MINUTOS))
elif TI == TF:
  print ('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')