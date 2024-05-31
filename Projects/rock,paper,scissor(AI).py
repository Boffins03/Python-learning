import random

def play_round():
    """Plays a single round of Rock-Paper-Scissors."""
    choices = ['rock', 'paper', 'scissors']
    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while player_choice not in choices:
        player_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)
    if player_choice == computer_choice:
        print("It's a tie!")
        return 0
    elif (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "paper" and computer_choice == "rock") or \
        (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        return 1
    else:
        print("Computer wins!")
        return -1

def play_game(num_rounds):
    """Plays a game of Rock-Paper-Scissors with the given number of rounds."""
    player_score = 0
    computer_score = 0
    for i in range(num_rounds):
        print("Round", i+1)
        result = play_round()
        if result == 1:
            player_score += 1
        elif result == -1:
            computer_score += 1
        print("Score: You", player_score, "- Computer", computer_score)
    if player_score > computer_score:
        print("You win the game!")
    elif player_score < computer_score:
        print("Computer wins the game!")
    else:
        print("The game ends in a tie!")    

print("Welcome to Rock-Paper-Scissors!")
num_rounds = int(input("How many rounds would you like to play? \n"))
play_game(num_rounds)
