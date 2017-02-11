from random import randint
hangmanPics=['''
  +----+
       |
       |
       |
    ====''','''

  +----+
  0    |
       |
       |
    ===='''.'''
  +----+
  0    |
  |    |
       |
    ====''','''
  +----+
  0    |
  |    |
 /|\   |
   =====''']

words='ant badger baboon beaver'.split()
print(words)
'''
def getRandomWord(wordList):
    
   
    wordIndex=random.randint(0,len(wordList)-1)
    return wordList[wordIndex)

a=(getRandomWord(words))
print(a)
'''
