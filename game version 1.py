import random
import os

def load_high_score():
    """Load the previous high score from file if exists."""
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", "r") as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return None
    return None

def save_high_score(score):
    """Save the new high score to file."""
    with open("high_score.txt", "w") as file:
        file.write(str(score))

def guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("Choose your difficulty level:")
    print("1. Easy (1–50)")
    print("2. Medium (1–100)")
    print("3. Hard (1–500)")

    # Select difficulty level
    level = input("Enter your choice (1/2/3): ")

    if level == "1":
        max_number = 50
    elif level == "2":
        max_number = 100
    elif level == "3":
        max_number = 500
    else:
        print("Invalid choice! Defaulting to Medium.")
        max_number = 100

    number_to_guess = random.randint(1, max_number)
    attempts = 0
    guess = None

    print(f"\nI'm thinking of a number between 1 and {max_number}. Try to guess it!")

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("📉 Too low! Try again.")
            elif guess > number_to_guess:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    # Score tracking
    high_score = load_high_score()
    if high_score is None or attempts < high_score:
        print("🏆 New High Score! Great job!")
        save_high_score(attempts)
    else:
        print(f"Your attempts: {attempts} | Current High Score: {high_score}")

# Run the game
guessing_game()
