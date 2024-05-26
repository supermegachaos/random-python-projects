#guess the number game
print( 'Hello! What is your name?')
guessesTaken = 0
import random
yourName = input()
number = random.randint ( 1 , 100)
print (' Well, ' + yourName + ' I am thinking of a number between 1 and 100')
for guessesTaken in range(6):
       print(' Take a guess. ') #four spaces in front of print
       guess = input()
       guess = int (guess)

       if guess < number:
           print ('Your guess is too low.') #nest the print statement

       if guess > number:
           print ('Your guess is too high.')

       if guess == number:
           break

if guess == number:
    guessesTaken = str( guessesTaken + 1)
    print ( ' Good Job,' +  yourName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
            
