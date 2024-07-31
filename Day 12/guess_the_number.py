
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100.")
import random
random_number = random.randint(1, 100)

difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
  print("You have 10 attempts to guess the number.")
  attempts = 10

  while attempts != 0:
    guess = int(input("Make a guess: "))
    if guess != random_number:
      attempts -= 1

      if guess < random_number:
        print("Too low.")
      else:
        print("Too high.")
      
      if attempts < 1 or attempts == 0:
        print("You've run out of attempts. You loose.")
        print(f"The answer was {random_number}")
      else:
        print(f"Guess again :] \nYou have {attempts} attempts left to guess the number.")
    else:
      print(f"You got it! the answer was {random_number}")
      break


elif difficulty == 'hard':
  print("You have 5 attempts to guess the number.")
  attempts = 5

  while attempts != 0:
    guess = int(input("Make a guess: "))
    if guess != random_number:
      attempts -= 1
      
      if guess < random_number:
        print("Too low.")
      else:
        print("Too high.")
      
      if attempts < 1 or attempts == 0:
        print("You've run out of attempts. You loose.")
        print(f"The answer was {random_number}")
      else:
        print(f"Guess again :] \nYou have {attempts} attempts left to guess the number.")
    else:
      print(f"You got it! the answer was {random_number}")
      break
else:
  print("You have to choose between 'easy' or 'hard'")








