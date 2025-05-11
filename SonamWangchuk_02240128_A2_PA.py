import random
import importlib  # Only moved this line up, no other changes

class Score:
    def __init__(self):
        self.scores = {
            "guess the number": 0,
            "rock paper scissors": 0,
            "answer": 0
        }

    def update_guess_the_number(self, attempts):
        self.scores["guess the number"] += max(0, 10 - attempts)

    def update_rock_paper_scissors(self):
        self.scores["rock paper scissors"] += 1

    def update_answer(self):
        self.scores["answer"] += 1

    def display(self):
        total = sum(self.scores.values())
        print("\nScores:")
        for game_name, score in self.scores.items():
            print(f"{game_name.capitalize()}: {score}")
        print(f"Total score: {total}")


class GuessTheNumber:
    def __init__(self, score):
        self.score = score

    def play(self):
        print("Guess the number between 1 to 10")
        number = random.randint(1, 10)
        attempts = 0
        while True:
            try:
                guess = int(input("Enter a random number: "))
                attempts += 1
                if guess == number:
                    print("You have guessed it correctly!")
                    self.score.update_guess_the_number(attempts)
                    break
                elif guess < number:
                    print("The number you have entered is too low.")
                else:
                    print("The number you have entered is too high.")
            except ValueError:
                print("Enter a valid number!")


class RockPaperScissors:
    def __init__(self, score):
        self.score = score

    def play(self):
        choices = ["rock", "paper", "scissors"]
        player = input("Choose rock, paper, or scissors: ").lower()
        if player not in choices:
            print("Invalid choice.")
            return
        computer = random.choice(choices)
        print(f"Computer chose: {computer}")
        if player == computer:
            print("Draw.")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
            self.score.update_rock_paper_scissors()
        else:
            print("You lose!")


class TriviaGame:
    def __init__(self, score):
        self.score = score
        self.questions = {
            "Science": { 
                "What type of blood cells help fight infections?": ("a. red blood cell", "b. white blood cell", "b")
            },
            "History": {
                "What is Bhutan's capital city?": ("a. Thimphu", "b. Paro", "a")
            }
        }

    def play(self):
        for category, quiz_set in self.questions.items():
            print(f"\nCategory: {category}")
            for quiz, options in quiz_set.items():
                print(quiz)
                for option in options[:2]:
                    print(option)
                user_answer = input("Your answer (a/b): ").lower()
                if user_answer == options[2]:
                    print("Excellent!")
                    self.score.update_answer()
                else:
                    print("Your answer is wrong.")


class GameManager:
    def __init__(self):
        self.score = Score()
        self.guess_the_number_game = GuessTheNumber(self.score)
        self.rock_paper_scissors_game = RockPaperScissors(self.score)
        self.trivia_game = TriviaGame(self.score)

    def pokemon_card_binder_manager(self):
        try:
            module = importlib.import_module("SonamWangchuk_02240128_A2_PB")
            if hasattr(module, "main"):
                module.main()  # This assumes the file has a main() function
            else:
                print("Module loaded, but no 'main()' function found.")
        except ModuleNotFoundError:
            print("Module 'Assignment2partB' not found.")

    def main_menu(self):
        while True:
            print("\nSelect a function (0-5):")
            print("1. Guess Number game")
            print("2. Rock paper scissors game")
            print("3. Trivia Pursuit Game")
            print("4. Pokemon Card Binder Manager")
            print("5. Check Current Overall score")
            print("0. Exit program")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.guess_the_number_game.play()
            elif choice == "2":
                self.rock_paper_scissors_game.play()
            elif choice == "3":
                self.trivia_game.play()
            elif choice == "4":
                self.pokemon_card_binder_manager()
            elif choice == "5":
                self.score.display()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.main_menu()