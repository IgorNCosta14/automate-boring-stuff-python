import random
 print ('Hello. what is your name?')
 name = input()

 print('well, ' + name + ', I am thinking of a number  between 1 and 20.')
 secretNumber = random.randint(1, 20)

 for guessesTaken in range(1, 7):
     print('Take a guess.')
     guess = int(input())

     if guess < secretNumber:
         print('Your guess is too low.')
     elif guess > secretNumber:
         print('Your guess is to high.')
     else:
         break
if guess == secretNumber:
    print('Good job, ' + name + 'you guessed my number in' + str(guessesTaken) + 'guesses!')
:
    print('Nope. The number i was thiking of was ' + secretNumber)
