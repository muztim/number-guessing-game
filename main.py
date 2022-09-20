from random import randint
from art import logo
HARD_LEVEL = 5
EASY_LEVEL = 10


# check the user's guess vs answer
def check_answer(guess, answer, attempt):
    if guess < answer:
        print("Too low")
        return attempt - 1
    if guess > answer:
        print("Too high")
        return attempt - 1
    else:
        print(f"You got it! The answer was {answer}.")


# ask the player to choose a difficulty level
def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def play_game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 101)

    attempt = difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {attempt} attempts left")
        guess = int(input("Make a guess: "))
        attempt = check_answer(guess, answer, attempt)
        if attempt == 0:
            print("You have run out of guesses, you lose")
            return
        else:
            print("Guess again.")


play_game()