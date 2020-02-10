from random import randint
value = randint(1,101)
print (value)

print ("GUESS THE NUMBER")
print ("Hello, do you wanna play ?")
guess = int(input ("Guess a number betwenn 1 and 100: "))

while guess != value:
    if guess > value:
        print ("Your guess is too high")
        guess = int(input ("Try again: "))
    elif guess < value:
        print ("Your guess is too low")
        guess = int(input ("Try again: "))

print ("You guessed the right number!")
