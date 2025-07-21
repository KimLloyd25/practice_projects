### THIS CODE IS A SIMPLE NUMBER GUESSING GAME WHERE THE USER CAN CHOOSE THE 2 VALUES THE COMPUTER MUST CHOOSE BETWEEN ###

#Import random module to randomise number later in code
import random

#Define variable and give value
play = True

#While variable is true, loop through
while play == True:
  #Define and set initial variables
  guess = 0
  number = 0
  min_num = 0
  max_num = 0

  #Display message to user
  print("Let's play a number guessing game.")
  #If variable is 0, ask user for a number. Display error if value is not a number and ask again until user provides a number
  while min_num == 0:
    try:
      min_num = int(input("Enter the lowest number I can choose: "))
    except ValueError:
      print("Invalid input. Please enter an integer.")

  #If variable is 0, ask user for a number. Display error if value is not a number and ask again until user provides a number
  while max_num == 0:
    try:
      max_num = int(input("Enter the highest number I can choose: "))
    except ValueError:
      print("Invalid input. Please enter an integer.")

  #Pick random number between to values and store in variable
  number = random.randint(min_num,max_num)
  #Display message to user
  print(f"I'm thinking of a number between {min_num} and {max_num}")
  #Request input from user to guess number. If input is not a number, display error and ask again until a number is entered.
  while guess == 0:
    try:
      guess = int(input("What number am I thinking of? "))
    except ValueError:
      print("Invalid input. Please enter an integer.")

  #If the users guess is the same as the random number picked, display winning message and ask if they would like to play again
  if guess == number:
    print(f"That's correct! It was {number}. You guessed right!")
    play = input("Would you like to play again? Y/N ")
    #If yes, set play variable to true, if not, set it to false and display game over message
    if play == "Y" or play == "y":
      play = True
    else:
      play = False
      print("GAME OVER")
  #If the users guess does not match the random number picked, display losing message and ask if they would like to play again
  else:
    print(f"That's incorrect. The number I was thinking of was {number}. Better luck next time!")
    play = input("Would you like to play again? Y/N ")
    #If yes, set play variable to true, if not, set it to false and display game over message
    if play == "Y" or play == "y":
      play = True
    else:
      play = False
      print("GAME OVER")
