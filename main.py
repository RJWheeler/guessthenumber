from random import randint
from art import logo
easy = 15
normal = 10
hard = 5


def check_answer(guess, answer, turns):
  if guess > answer:
    print(f"{guess} was too high.")
    return turns - 1
  elif guess < answer:
    print(f"{guess} was too low")
    return turns - 1
  else:
    print(f"{answer} was correct. You win")


def difficulty():
  correct_input = False
  while not correct_input:
    level = input("Choose a difficulty. Type 'easy', 'normal', or 'hard': ").lower()
    if level == "easy":
      correct_input = True
      return easy
    elif level == "normal":
      correct_input = True
      return normal
    elif level == "hard":
      correct_input = True
      return hard
    else:
      print("Please put in the correct input.")


def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1,100)
  turns = difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number")
    guess = int(input("Guess the number: "))
    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
play_again = False
play_again_input = input("Would you like to play again? Type 'y' or 'n'").lower()
if play_again_input == "y":
  play_again = True
while play_again:
  game()
  play_again_input = input("Would you like to play again? Type 'y' or 'n'").lower()
  if play_again_input == "n":
    play_again = False
print("Thanks for playing")