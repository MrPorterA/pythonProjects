import random
hangmanPics= [
'  +---+   \n  |   |   \n      |   \n      |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n      |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n  |   |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|   |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n /    |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n / \\  |   \n      |   \n========= \n'
]

words='ant badger baboon beaver'.split()
print(words)

def getRandomWord(wordList):
    
   
    wordIndex=random.randint(0,len(wordList)-1)
    return wordList[wordIndex]



def getGuess(alreadyGuessed):
    while True:
        print('guess a letter')
        guess=input()
        guess=guess.lower()
        if len(guess)!=1:
            print('please type a single letter')
        elif guess in alreadyGuessed:
            print('you have already guessed that letter')
        else:
            return guess
def displayBoard(missedLetters,correctLetters,secretWord):
    print(hangmanPics[len(missedLetters)])
    print()

    blanks='_'*len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks=blanks[:i]+secretWord[i]+blanks[i+1:]

    for letter in blanks:
        print(letter,end='')

    print()


## main program
print('HANGMAN')
missedLetters=''
correctLetters=''
secretWord=(getRandomWord(words))
gameIsDone=False

while True:
    displayBoard(missedLetters,correctLetters,secretWord)
    print(secretWord)
    guess=getGuess(missedLetters+correctLetters)

    if guess in secretWord:
        correctLetters=correctLetters+guess
        
        foundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False
                break
        if foundAllLetters:
            print('yes you have won')
            gameIsDone=True

    else:
        missedLetters=missedLetters+guess

        if len(missedLetters)>len(hangmanPics):
            print('you have guessed too many times')
            gameIsDone=True
        
        
    
