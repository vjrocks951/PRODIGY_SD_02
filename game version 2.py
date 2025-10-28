import tkinter as tk
from tkinter import messagebox
import random
import os

# --- Helper functions for high score tracking ---
def load_high_score():
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", "r") as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return None
    return None

def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))

# --- Main Game Class ---
class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Number Guessing Game")
        self.root.geometry("400x400")
        self.root.configure(bg="#222831")

        self.number_to_guess = None
        self.attempts = 0
        self.max_number = 100

        self.create_welcome_screen()

    def create_welcome_screen(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="🎯 Number Guessing Game", font=("Arial", 18, "bold"),
                 fg="#00ADB5", bg="#222831").pack(pady=20)

        tk.Label(self.root, text="Choose Difficulty Level:", font=("Arial", 12),
                 fg="white", bg="#222831").pack(pady=10)

        tk.Button(self.root, text="Easy (1–50)", width=20, command=lambda: self.start_game(50),
                  bg="#00ADB5", fg="white").pack(pady=5)
        tk.Button(self.root, text="Medium (1–100)", width=20, command=lambda: self.start_game(100),
                  bg="#00ADB5", fg="white").pack(pady=5)
        tk.Button(self.root, text="Hard (1–500)", width=20, command=lambda: self.start_game(500),
                  bg="#00ADB5", fg="white").pack(pady=5)

    def start_game(self, max_number):
        self.max_number = max_number
        self.number_to_guess = random.randint(1, max_number)
        self.attempts = 0

        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Guess a number between 1 and {max_number}",
                 font=("Arial", 14, "bold"), fg="#00ADB5", bg="#222831").pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10)

        tk.Button(self.root, text="Submit Guess", command=self.check_guess,
                  bg="#00ADB5", fg="white", font=("Arial", 12)).pack(pady=10)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12),
                                       fg="white", bg="#222831")
        self.feedback_label.pack(pady=10)

        self.attempts_label = tk.Label(self.root, text="Attempts: 0", font=("Arial", 12),
                                       fg="#EEEEEE", bg="#222831")
        self.attempts_label.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback_label.config(text="⚠️ Please enter a valid number!", fg="orange")
            return

        guess = int(guess)
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.number_to_guess:
            self.feedback_label.config(text="📉 Too low! Try again.", fg="#F0A500")
        elif guess > self.number_to_guess:
            self.feedback_label.config(text="📈 Too high! Try again.", fg="#F0A500")
        else:
            self.feedback_label.config(text=f"🎉 Correct! You guessed it in {self.attempts} attempts.",
                                       fg="#00FF00")
            self.check_high_score()

    def check_high_score(self):
        high_score = load_high_score()
        if high_score is None or self.attempts < high_score:
            save_high_score(self.attempts)
            messagebox.showinfo("🏆 New High Score!", f"🎉 You set a new record with {self.attempts} attempts!")
        else:
            messagebox.showinfo("✅ Game Over", f"You guessed it in {self.attempts} attempts.\n"
                                               f"Current High Score: {high_score}")

        self.ask_play_again()

    def ask_play_again(self):
        play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if play_again:
            self.create_welcome_screen()
        else:
            self.root.destroy()

# --- Run the Game ---
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGame(root)
    root.mainloop()
