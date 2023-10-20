from getpass import getpass as input

print("Le Gand Jeu")


# Player 1 input
player1 = input("Player 1, enter your name: ")
print(f"welcome {player1}")
player2 = input("Player 2, enter your name: ")
print(f"welcome {player2}")
print()

player1_choice = input(f"{player1}, choose rock, paper, or scissors: ")
print()
# Player 2 input
player2_choice = input(f"{player2}, choose rock, paper, or scissors: ")
print()
# Determine the winner
if player1_choice == "rock":
  if player2_choice == "rock":
    print("You both picked Rock, draw !")
  elif player2_choice == "paper" : 
    print(f"{player1} is lose ")
    print(f"{player1} is wins !")
  elif player2_choice == "scissors":
    print("Player1's Rock is smothered by Player2's Paper!")
  else:
    print("Invalid Move Player 2!")
elif player1_choice == "paper":
  if player2_choice == "rock":
     print(f"{player2} is wins")
  elif player2_choice == "scissors":
     print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
  elif player1_choice == "paper":
     print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
elif player1_choice == "scissors":
    if player2_choice == "rock":
      print(f"{player1} Rock makes metal-dust out of Player1's Scissors")
elif player1_choice=="S":
    print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
elif player1_choice=="P":
    print("Player1's Scissors make confetti out of Player2's paper!")
else:
    print("Invalid Move Player 2!")
      
      
    