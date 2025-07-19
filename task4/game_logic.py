# game_logic.py

import random

CHOICES = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return random.choice(CHOICES)

def get_winner(player_choice, computer_choice):
    player_choice = player_choice.capitalize()
    computer_choice = computer_choice.capitalize()

    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "Player"
    else:
        return "Computer"

