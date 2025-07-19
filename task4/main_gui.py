# main_gui.py

import tkinter as tk
from game_logic import get_computer_choice, get_winner

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Emoji map
        self.emoji_map = {
            "Rock": "🪨",
            "Paper": "📄",
            "Scissors": "✂️"
        }

        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0

        # Title
        tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold")).pack(pady=10)

        # Scoreboard
        self.score_label = tk.Label(root, text=self.get_score_text(), font=("Arial", 14))
        self.score_label.pack(pady=10)

        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Emoji display
        self.player_choice_label = tk.Label(root, text="", font=("Arial", 40))
        self.player_choice_label.pack(pady=5)

        self.computer_choice_label = tk.Label(root, text="", font=("Arial", 40))
        self.computer_choice_label.pack(pady=5)

        # Buttons
        for choice in ["Rock", "Paper", "Scissors"]:
            btn = tk.Button(root, text=choice, font=("Arial", 12), width=15,
                            command=lambda c=choice: self.play(c))
            btn.pack(pady=5)

    def get_score_text(self):
        return f"Player: {self.player_score} | Computer: {self.computer_score} | Ties: {self.tie_score}"

    def play(self, player_choice):
        player_choice = player_choice.capitalize()
        computer_choice = get_computer_choice()

        winner = get_winner(player_choice, computer_choice)

        # Update scores
        if winner == "Player":
            self.player_score += 1
            result = "You Win!"
        elif winner == "Computer":
            self.computer_score += 1
            result = "Computer Wins!"
        else:
            self.tie_score += 1
            result = "It's a Tie!"

        # Update GUI
        self.result_label.config(text=result)
        self.score_label.config(text=self.get_score_text())
        self.player_choice_label.config(text=f"You: {self.emoji_map[player_choice]}")
        self.computer_choice_label.config(text=f"Computer: {self.emoji_map[computer_choice]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGame(root)
    root.mainloop()
