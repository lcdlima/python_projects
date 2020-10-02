# You must make a program that reads any value and presents a message saying in which of the following intervals ([0.25], (25.50], (50.75], (75.100]) this value is found. the value is not in any of these ranges, the message “Out of range” should be printed.
# The symbol (represents "greater than". For example:
#   [0.25] indicates values between 0 and 25.0000, including them.
#   (25.50] indicates values greater than 25 Ex: 25.00001 up to the value 50.0000000

N = float(input())

if N >= 0 and N <=25:
    print ('Intervalo [0,25]')
elif N>25 and N<=50:
    print ('Intervalo (25,50]')
elif N>50 and N<=75:
    print ('Intervalo (50,75]')
elif N>75 and N<=100: 
    print ('Intervalo (75,100]')
else:
    print ('Fora de intervalo')