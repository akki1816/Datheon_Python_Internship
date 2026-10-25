
import random

WORDS = ["PYTHON", "CODING", "GITHUB", "COMPUTER", "PROGRAM"]

STAGES = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]


def play_hangman():
    word = random.choice(WORDS)
    guessed = set()
    wrong = set()
    max_attempts = 6

    print("Welcome to Hangman!")

    while len(wrong) < max_attempts:
        display = " ".join(
            letter if letter in guessed else "_"
            for letter in word
        )

        print(STAGES[len(wrong)])
        print("Word:", display)
        print("Wrong guesses:", ", ".join(sorted(wrong)) or "None")
        print("Attempts left:", max_attempts - len(wrong))

        if all(letter in guessed for letter in word):
            print("Congratulations! You won!")
            return

        guess = input("Guess one letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter one letter from A to Z.")
            continue

        if guess in guessed or guess in wrong:
            print("You already guessed that letter!")
            continue

        if guess in word:
            guessed.add(guess)
            print("Correct!")
        else:
            wrong.add(guess)
            print("Incorrect!")

    print(STAGES[max_attempts])
    print("Game over! The word was:", word)


if __name__ == "__main__":
    play_hangman()
