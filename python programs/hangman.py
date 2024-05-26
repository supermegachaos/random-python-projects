import random
HANGMAN_PICS = [
'''
+----+
     l
     l
     l
    === ''',
'''
+----+
     1
     1
     1
    ===''',
'''
 +---+
 O   l
     l
     l
    ===''',
'''
 +---+
 O   l
 1   l
     l
    ===''',
'''
 +---+
 O   l
 1   l
/    l
    ===''',
'''
 +---+
 O   l
 1   l
/ \  l
    ===''',
'''
 +---+
 O   l
 1\  l
/ \  l
    ===''',
'''
 +---+
 O   l
/1\  l
/ \  l
    ===''']
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
crow deer dog donkey duck eagle ferret fox frog goat goose hawk parrot pigeon python
rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey
turtle weasel whale wolf wombat zebra'''.split()

def getRandomWord(wordList):
    #this funtion returns a random string from the list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard (missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ' )
    print()

    blanks = ['_'] * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

# convert blanks list back to string
    blanks_str = ''.join(blanks)
    print(blanks_str)

# show the secret word with spaces in between each letter
    for letter in blanks:
        print(letter, end=' ')
print()

def getGuess(alreadyGuessed):
        #returns the letter the player entered. this funtion make sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print(' You have guessed that letter. choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    #this function returns true if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again?(yes or no)')
    return input().lower().startswith('y')



print('H A N G M A N')
missedLetters = ' '
correctLetters = ' '
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    #let the player guess a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for letter in secretWord:
            if letter not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        #cheack if player guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' Correct guesses, the word was"' + secretWord+ '"')
            gameIsDone = True

            #ask do you want to play again (but only if the game is done)
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone= False
                secretWord= getRandomWord(words)
            else:
                break
