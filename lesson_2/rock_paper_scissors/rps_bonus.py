# rock paper scissors
import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

WINNING_RULES = {
    'scissors': ['paper', 'lizard'],
    'paper': ['rock', 'spock'],
    'rock': ['lizard', 'scissors'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock'],
}

def winning_player(player1, player2):
    return player2 in WINNING_RULES.get(player1, [])

def display_winner(player, computer):
    if winning_player(player, computer):
        return "You Win!"
    if winning_player(computer, player):
        return "Computer Wins"

    return "It's Tied"

# prompt function works without errors
def prompt(message):
    print(f'==> {message}')

# bonus feature: get shortened input
# for spock: using 'sp'
def get_input():
    players_choice = input()

    match players_choice:
        case 'r':
            return 'rock'
        case 'p':
            return 'paper'
        case 's':
            return 'scissors'
        case 'l':
            return 'lizard'
        case 'sp':
            return 'spock'
        case _:
            return 'invalid input'

def display_choice(choices_list):
    prompt(f"Welcome to {', '.join(choices_list).upper()}!")

    for choices in choices_list:
        if choices == 'spock':
            prompt(f"Press '{choices[0:2]}' for {choices}")
        else:
            prompt(f"Press '{choices[0]}' for {choices}")

def display_score(player1_score, player2_score):
    prompt("Current Score: ")
    prompt(f"You: {player1_score}")
    prompt(f"Computer: {player2_score}")

def play_game():
    player_score = 0
    computer_score = 0
    play_again = True

    while play_again:
        display_choice(VALID_CHOICES)
        choice = get_input()

        while choice not in VALID_CHOICES:
            prompt("That's not a valid choice")
            choice = get_input()

        computer_choice = random.choice(VALID_CHOICES)

        prompt(f"You chose {choice}. Computer chose {computer_choice}")

        # add prompt function to display winner
        prompt(display_winner(choice, computer_choice))

        # Bonus feature: keeping score
        if winning_player(choice, computer_choice):
            player_score += 1
            display_score(player_score, computer_score)
            if player_score == 3:
                prompt("You've WON!")
                break
        elif winning_player(computer_choice, choice):
            computer_score += 1
            display_score(player_score, computer_score)
            if computer_score == 3:
                prompt("Computer WON!")
                break

        prompt("play again? (y/n)")
        answer = input().lower()

        while True:
            if answer.startswith('y') or answer.startswith('n'):
                break

            prompt("Please enter 'y' or 'n'.")
            answer = input().lower()

        # rewrite the loop, so break statement is not used
        if answer[0] == 'n':
            play_again = False

play_game()