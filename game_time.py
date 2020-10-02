# Read the start and end times of a game. Then calculate the duration of the game, knowing that it can start on one day and end on another, with a minimum duration of 1 hour and a maximum of 24 hours.

ENTRADA = input().split()

HI = int(ENTRADA[0])
HF = int(ENTRADA[1])

if HI < HF:
    print ('O JOGO DUROU {} HORA(S)'.format (HF-HI))
elif HI > HF: 
    print ('O JOGO DUROU {} HORA(S)'.format (24 - HI + HF))
elif HI == HF:
    print ('O JOGO DUROU 24 HORA(S)')