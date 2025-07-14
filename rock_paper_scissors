#This is a game of Rock, Paper, Scissors

#Import randint from random to use to randomly select a value from options
from random import randint

#Set play variable
play = "Y"

#Set the options variable to collection of options
options = ["Rock", "Paper", "Scissors"]

#Randomly select a value from options for the computer
computer = options[randint(0,2)]

#Loop through game
while (play == "Y" or "y"):

  #Ask player for their choice of rock, paper or scissors
  player = input("Rock, paper, scissors? ")

  #If statements to decide winner of game and output messages
  if player == computer:
    print("It's a tie!")
  elif player == "Rock":
    if computer == "Paper":
      print(f"You lose! {computer} covers {player}")
    else:
      print(f"You win! {player} smashes {computer}")
  elif player == "Paper":
    if computer == "Rock":
      print(f"You win! {player} covers {computer}")
    else:
      print(f"You lose! {computer} cuts {player}")
  elif player == "Scissors":
    if computer == "Rock":
      print(f"You win! {player} smashes {computer}")
    else:
      print(f"You lose! {computer} cuts {player}")
  else:
    print("Invalid choice. Try again.")
  
  #Reset player choice variable
  player = ""
  
  #Ask player if they want to play again
  play = input("Would you like to play again? (Y/N) ")
  if play == "Y":
    continue
  elif play == "y":
    continue
  else:
    print("GAME OVER")
    break
