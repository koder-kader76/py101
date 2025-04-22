# rock paper scissors
import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

# display_winner returning strings 
def display_winner(player, computer):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')):
        return "You win!"
    elif ((computer == 'rock' and player == 'scissors') or
        (computer == 'paper' and player == 'rock') or
        (computer == 'scissors' and player == 'paper')):
        return "Computer wins!"
    else:
        return "It's a tie!"

# prompt function works without errors
def prompt(message):
    print(f'==> {message}')

play_again = True

while play_again:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {choice}. Computer chose {computer_choice}")

    # add prompt function to display winner
    prompt(display_winner(choice, computer_choice))

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