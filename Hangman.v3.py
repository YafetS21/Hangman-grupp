# Importing random module to randomize a word from wordlist
import random

# Read lines in file, the file contains word that the game can use
with open('wordlist2.txt', 'r') as f:
    # Reads and store the lines in a list called words
    words = f.readlines()


#   The class contains methods to manage the game
#   Choose a word, show the word, make guesses and decide if the game is over
class HangmanGame:
    # Constructor takes two arguments: wordlist2_filename, errors_allowed=7
    def __init__(self, wordlist2_filename, errors_allowed=7):
        # Sets the number of errors allowed to errors_allowed
        self.errors_allowed = errors_allowed
        # Initializes an empty list to store the player's guesses
        self.guesses = []
        # Initializes a flag to indicate if the game is over
        self.done = False
        # Opens the file wordlist2_filename for reading
        with open(wordlist2_filename, 'r') as e:
            # Reads all the lines in the file wordlist2_filename and stores them in a list called self.words
            self.words = e.readlines()

        # Randomly selects a word from the dictionary and stores it in self.word
        self.word = random.choice(self.words).strip()

    # Returns a string representing the current word
    # The string contains an underscore for each letter in the word that the player has not yet guessed
    def display_word(self):
        # An empty string is initialized to store the current word
        displayed_word = ""
        # A for loop iterates over all the letters in the word self.word
        for letter in self.word:
            # For each letter in the word, it is checked whether the letter is in the self.guesses list.
            if letter.lower() in self.guesses:
                # If the letter is in the list, the letter is added to the displayed_word string.
                displayed_word += letter + " "
            # Otherwise, an underscore is added to the displayed_word string.
            else:
                displayed_word += "_ "
        # After the for loop completes, the string displayed_word is returned
        return displayed_word

    # Adds the guessing guess to the list self.guesses
    # If guess is not in the word self.word, self.errors_allowed decreases by 1
    def make_guess(self, guess):
        guess = guess.lower()
        self.guesses.append(guess)
        if guess not in self.word.lower():
            self.errors_allowed -= 1

    # Returns True if the game is over, False otherwise
    # The game is over if the player has made the self.errors_allowed number of mistakes
    # or if the player has guessed all the letters in the word self.word.
    def is_game_over(self):
        if self.errors_allowed == 0:
            self.done = True
            return True
        elif all(letter.lower() in self.guesses for letter in self.word):
            self.done = True
            return True
        return False


# The main feature of the game.
# The function creates an instance of the HangmanGame class and then starts the game.
def main():
    wordlist2_filename = 'wordlist2.txt'
    # Creates an instance of the HangmanGame class with the wordlist2.txt file as the wordlist.
    game = HangmanGame(wordlist2_filename)
    # As long as the game is not over, the following code is executed:
    # Display the current word.
    # Ask the player for a guess.
    # Make the guess.
    # Om inte spelet fortsätter så visas display
    while not game.is_game_over():
        print(game.display_word())
        guess = input(f"Allowed errors left: {game.errors_allowed}, Guess a letter: ")
        game.make_guess(guess)

    if all(letter.lower() in game.guesses for letter in game.word):
        print(f"You found the word! It was '{game.word}'!")
    else:
        print(f"Game over! The word was '{game.word}'!")


if __name__ == "__main__":
    main()
