from enum import Enum
import inquirer
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
        self.attempts =  self.DifficultyLevel[difficulty].value
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
    def make_guess(self):
        print("Attempts left:", self.attempts_left)
        guess = input("Try to guess: ").lower()

        if not self.is_valid_guess(guess):
            print(f"Entered: {guess}, Result: Invalid character!")
            return True

        if self.is_correct_full_guess(guess):
            print(f"Entered: {guess}, Result: Correct guess!")
            self.reveal_entire_word(guess)
            return True

        if len(guess) == 1:
            return self.process_single_letter_guess(guess)
        
        print(f"Entered: {guess}, Result: Incorrect guess!")
        return False

    def is_valid_guess(self, guess):
        return all(char in self.allowed_characters for char in guess)

    def is_correct_full_guess(self, guess):
        return guess == ''.join(self.word_to_guess)

    def reveal_entire_word(self, guess):
        self.word_to_guess = [None for _ in self.word_to_guess]
        self.current_word_state = list(guess)

    def process_single_letter_guess(self, letter):
        if letter in self.word_to_guess:
            print(f"Entered: {letter}, Result: Correct guess!")
            first_occurrence = self.word_to_guess.index(letter)
            self.word_to_guess[first_occurrence] = None
            self.current_word_state[first_occurrence] = letter
            return True
        else:
            print(f"Entered: {letter}, Result: Incorrect guess!")
            self.attempts_left -= 1
            return False




        
            
        
        
        
        print(f"Entered: {guess}, Result: Incorrect guess!")
        return False




    def play(self):
    
        
        self.initialize_word()
        attempts_left = self.attempts
        
        while(attempts_left>0 and not self.is_win):
           
            if self.make_guess():
                self.is_win = self.check_win()
            else:
                attempts_left -= 1

            print("Word: "," ".join(self.current_word_state))


        print("Game result: ", "Vicory" if self.is_win else "Defeat", "with ")
        
    


h = Hangman()





