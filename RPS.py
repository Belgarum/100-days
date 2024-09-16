import random

choices = ['rock', 'paper', 'scissors']

player_choice = input('Pressd enter to start!').lower()

comp_choice = random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "player"
    else:
        return "computer"

    
player_wins = 0
computer_wins = 0

while True:
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

    if player_choice == 'quit':
        break
    
    if player_choice not in choices:
        print("Invalid input. Please try again.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    
    if result == "player":
        print("You win!")
        player_wins += 1
    elif result == "computer":
        print("Computer wins!")
        computer_wins += 1
    else:
        print("It's a tie!")
    
    print(f"Score: Player {player_wins} - Computer {computer_wins}")