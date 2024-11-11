from enum import Enum
import inquirer
import msvcrt 
import string
from random_word import RandomWords

class Game:
    def __init__(self, players):
        self.players = players
        self._play()
    
    def _play(self):
        print("Game has started...")

class Hangman(Game):

    allowed_characters = set(string.ascii_lowercase)
    class DifficultyLevel(Enum):
        BEGGINER = 8
        INTERMEDIATE = 5
        ADVANCED = 3

    def __init__(self):
        players = int(self.get_game_info("Choose number of players", ['1', '2']))
        difficulty = self.get_game_info("Choose difficulty ", [level.name for level in self.DifficultyLevel])
        self.difficulty = difficulty
        super().__init__(players)
        self.is_win = False
        self.play()

    def get_game_info(self, message, choices):
        questions = [
            inquirer.List('choice',
                        message=message,
                        choices=choices,
                        ),
        ]
        answer = inquirer.prompt(questions)
        return answer['choice']

    def initialize_word(self):
            if self.players == 1:
                word_generator = RandomWords()
                word = word_generator.get_random_word()
            else:
                word = input("Enter word: ")
            self.word_to_guess = list(word)
            self.current_word_state = ['_'] * len(word)
            print("Word to guess: ", " ".join(self.current_word_state))

    def check_win(self):
        return all(char is None for char in self.word_to_guess) 
    def check_guess(self, guess):

        if guess in self.word_to_guess:
            print(f"Entered: {guess}, Result: Correct guess!")
            first_occurence = self.word_to_guess.index(guess)
            self.word_to_guess[first_occurence] = None
            self.current_word_state[first_occurence] = guess
            return True
        

        print(f"Entered: {guess}, Result: Incorrect guess!")
        return False

    def play(self):

        
        self.initialize_word()
        attempts_left = self.DifficultyLevel[self.difficulty].value
        
        while(attempts_left>0 and not self.is_win):
            print("Attempts left: ", attempts_left)
            guess = input("Try to guess: ").lower()

            if len(guess) !=1 or guess not in self.allowed_characters:
                print("Invalid input - only single letters from asci are allowed")
                continue

            if self.check_guess(guess):
                self.is_win = self.check_win()
            else:
                attempts_left -= 1

            print("Word: "," ".join(self.current_word_state))


        print("Game result: ", "Vicory" if self.is_win else "Defeat", "with ")
        
    

h = Hangman()





