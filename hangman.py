### This is a simple hangman game where the user has to guess a randomly selected word (from a list). ###
### The user has 6 lives and each incorrect guess removes a life. The game ends when the user ###
### guesses the word or runs out of lives. ###


#Import from library in order to randomly select a word from the words list
from random import choice

#Set global variables
lives = 6
answer = []
guessed_letters = []

#Create list of words, choose one at random and create the _ _ _ _ hangman variable
def get_random_word():
    global answer
    words = ['coat','jump','river','tennis','card','holiday','python','laptop','guitar','piano','house','garden','bottle','window','rocket','jumper','monkey','rain','phone','camera','kitchen','forest','island','desert','ocean','mountain','bridge','castle','school','balloon','station','airport','library','jelly','cinema','cafe','hotel','beach']
    word = choice(words)
    
    for l in word:
        answer.append("_")
    print(f"The word you need to guess is: {' '.join(answer)}")
    
    return word, answer

#Ask the user to guess a letter
def ask_letter():
    letter = input("Guess a letter: ").lower()
    return letter

#Check the letter is a letter and hasn't been previously guessed. One validated, call check_letter or display error
def validate_letter(letter, word, guessed_letters):
    if letter.isalpha() and letter not in guessed_letters:
        guessed_letters.append(letter)
        check_letter(letter, word)
    elif not letter.isalpha():
        print("This is not a valid guess. Please try again.")
    elif letter in guessed_letters:
        print(f"You've already guessed the letter {letter} - please choose another letter")

#Check if the letter is in the word. If so, amend the answer variable and replace the correct list item(s) with the correct letter
#If not in the word, remove a life and notify user
def check_letter(letter, word):
    global answer, lives
    ind = 0
    
    if letter in word:
        
        for i in word:
            if i == letter:
                answer[ind] = letter
                ind += 1
            else:
                ind += 1
                continue
        
        print(f"{letter} is in the word {' '.join(answer)}")
    else:
        lives -= 1
        print(f"{letter} is not in the word {' '.join(answer)}. You only have {lives} left.")
    if ''.join(answer) == word:
                print(f"Amazing, you guessed the word: {word}")

#Call function to get a random word and store word and answer in variables
word, answer = get_random_word()

#While loop iterates while the answer does not match the random word, and while lives still exist
#It calls 2 functions, as below
while ''.join(answer) != word and lives != 0:
    letter = ask_letter()
    validate_letter(letter, word, guessed_letters)
    
#Once the lives have run out, display a message to the user depending on the outcome of theh game
if answer == word:
    print(f"Amazing, you guessed the word: {word}")
else:
    print(f"You're out of lives. The word was: {word}")
