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
    gameNum = int(input("# Type here the number of matches you'd like to play: "))
    # Initial score
    plWins = 0
    cpWins = 0

    # Rock, Paper, Scissors matches loop
    for x in range(1, gameNum+1):
        print(f'# MATCH NUMBER {x} #')                  # Match counter
        player = input("Player choice: ")               # Player choice
        computer = random.choice(["r", "s", "p"])
        print(f'Computer choice: {computer}')           # Computer choice

        # Win conditions check
        if player == computer:
            print("Pair!")
            plWins += 0
            cpWins += 0
        elif player == "r" and computer == "s":
            print("# PLAYER WINS!")
            plWins += 1
        elif player == "s" and computer == "p":
            print("# PLAYER WINS!")
            plWins += 1
        elif player == "p" and computer == "r":
            print("# PLAYER WINS!")
            plWins += 1
        else:
            print("# COMPUTER WINS!")
            cpWins += 1

    # Score output
    print("# FINAL SCORE #")
    print(f'PLAYER: {plWins}, COMPUTER: {cpWins}')
    if plWins > cpWins:
        print("PLAYER WINS!")
    elif plWins == cpWins:
        print("DRAW GAME!")
    else:
        print("COMPUTER WINS!")

    # Play again / exit option
    new_game = input("Would you like to play again? [y/n] ")
    if new_game == "y":
        gameset()           # Restart game
    else:
        print("Goodbye!")
        exit                # Exit game


# Game function
gameset()



