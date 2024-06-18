import random

# ROCK, SCISSORS, PAPER GAME
# PLAYER VS COMPUTER

# Number of matches
print("# ROCK / SCISSORS / PAPER GAME #")
print("# RULES: r for rock // s for scissors // p for paper")


# Game function
def gameset():
    # Initial settings
    # Number of matches
    game_num = int(input("# Type here the number of matches you'd like to play: "))
    # Initial score
    player_wins = 0
    computer_wins = 0

    # Rock, Paper, Scissors matches loop
    for x in range(1, game_num+1):
        print(f'# MATCH NUMBER {x} #')                  # Match counter
        player = input("Player choice: ")               # Player choice
        computer = random.choice(["r", "s", "p"])
        print(f'Computer choice: {computer}')           # Computer choice

        # Win conditions check
        if player == computer:
            print("Pair!")
            player_wins += 0
            computer_wins += 0
        elif player == "r" and computer == "s":
            print("# PLAYER WINS!")
            player_wins += 1
        elif player == "s" and computer == "p":
            print("# PLAYER WINS!")
            player_wins += 1
        elif player == "p" and computer == "r":
            print("# PLAYER WINS!")
            player_wins += 1
        else:
            print("# COMPUTER WINS!")
            computer_wins += 1

    # Score output
    print("# FINAL SCORE #")
    print(f'PLAYER: {player_wins}, COMPUTER: {computer_wins}')
    if player_wins > computer_wins:
        print("PLAYER WINS!")
    elif player_wins == computer_wins:
        print("DRAW GAME!")
    else:
        print("COMPUTER WINS!")

    # Play again / exit option
    new_game = input("Would you like to play again? [y/n] ")
    if new_game == "y":
        gameset()           # Restart game
    else:
        print("Goodbye!")
        exit()                # Exit game


# Game function
gameset()
