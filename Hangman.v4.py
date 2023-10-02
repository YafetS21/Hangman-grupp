import random

# Read lines in file, the file contains words that the game can use
with open('wordlist2.txt', 'r') as f:
    # Reads and store the lines in a list called words
    words = f.readlines()

# Define the HangmanGame class
class HangmanGame:
    def __init__(self, wordlist2_filename, errors_allowed=7):
        self.errors_allowed = errors_allowed
        self.guesses = []
        self.done = False

        # Reads all the lines in the file wordlist2_filename and stores them in a list called self.words
        with open(wordlist2_filename, 'r') as e:
            self.words = e.readlines()

        # Randomly selects a word from the dictionary and stores it in self.word
        self.word = random.choice(self.words).strip()

        # Initialize hangman stages
        self.hangman_stages = [
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            """
        ]

    def display_hangman(self):
        # Display the appropriate hangman stage based on errors_allowed
        return self.hangman_stages[7 - self.errors_allowed]

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter.lower() in self.guesses:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        return displayed_word

    def make_guess(self, guess):
        guess = guess.lower()
        self.guesses.append(guess)
        if guess not in self.word.lower():
            self.errors_allowed -= 1

    def is_game_over(self):
        if self.errors_allowed == 0:
            self.done = True
            return True
        elif all(letter.lower() in self.guesses for letter in self.word):
            self.done = True
            return True
        return False

# The main game loop
def main():
    wordlist2_filename = 'wordlist2.txt'
    game = HangmanGame(wordlist2_filename)

    while not game.is_game_over():
        print(game.display_word())
        print(game.display_hangman())  # Display the hangman figure
        guess = input(f"Allowed errors left: {game.errors_allowed}, Guess a letter: ")
        game.make_guess(guess)

    if all(letter.lower() in game.guesses for letter in game.word):
        print(f"You found the word! It was '{game.word}'!")
    else:
        print(f"Game over! The word was '{game.word}'!")

if __name__ == "__main__":
    main()
