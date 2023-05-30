# import randomint from random
from random import randint

# introduction
print("Welcome to Rock Paper Scissors!")

#
while True:

  # separate main game from intro
  input("\nPress 'enter' to start!\n")
  
  # game choices
  choices = ['rock', 'paper', 'scissors']
  
  # grab player choice
  playerChoice = input("Choose your weapon. Enter 'rock', 'paper' or 'scissors':\n")
  
  computerChoice = choices[randint(0,2)]
  
  match playerChoice:
      case "rock":
        print(f"You chose rock. The computer chooses {computerChoice}.")
        if computerChoice == "rock":
          print("It's a tie!")
        elif computerChoice == "paper":
          print("You lose!")
        else:
          print("You win!")
  
      case "paper":
        print(f"You chose paper. The computer chooses {computerChoice}.")
        if computerChoice == "paper":
          print("It's a tie!")
        elif computerChoice == "scissors":
          print("You lose!")
        else:
          print("You win!")
  
      case "scissors":
        print(f"You chose scissors. The computer chooses {computerChoice}.")
        if computerChoice == "scissors":
          print("It's a tie!")
        elif computerChoice == "rock":
          print("You lose!")
        else:
          print("You win!")
  
      case _:
        print("Your input is incorrect, please try again.")

  # restart option
  restart = input("\nDo you want to play again? Enter 'yes' to continue or any other key to exit:\n")
  if restart != "yes":
        break

      