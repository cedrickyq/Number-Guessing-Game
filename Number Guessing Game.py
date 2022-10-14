# Import of libraries
import random2
from termcolor import colored


# Display of options
def Display():
  print(colored("\nOptions:\n--------\n0: Exit\n1: Easy\n2: Hard\n\nEasy: Numbers: 0-15, Guesses: 3\nHard: Numbers: 0-30, Guesses: 5", "blue"))
  Input()


# Input of option
def Input():
  global Option
  Option = input(colored("\nOption: ", "blue"))
  Options()


# Sorting of options
def Options():
  if Option == "0":
    Exit()
  elif Option == "1":
    Easy()
  elif Option == "2":
    Hard()
  else:
    print(colored("\nInvalid input.", "red"))
    Display()


# Exit
def Exit():
  print(colored("\nScript exiting...", "red"))
  exit()


# Easy
def Easy():
  Generated_number = random2.randrange(0, 15)
  Guesses = 3
  Tries = 0
  print(colored("\nEasy:\n-----", "blue"))
  while Tries < Guesses:
    try:
      Tries += 1
      Guess = int(input(colored("\nGuess: ", "blue")))
      if Guess == Generated_number:
        print(colored("\nYou won.", "red"))
        print(colored(f"\nNumber entered: {Guess}", "green"))
        print(colored(f"\nNumber of tries used: {Tries}", "green"))
        Display()
      elif Guess < Generated_number:
        print(colored("\nNumber entered lower than generated number.", "green"))
        print(colored(f"\nNumber entered: {Guess}", "green"))
        Tries_left = Guesses - Tries
        print(colored(f"\nNumber of tries left: {Tries_left}", "green"))
      elif Guess > Generated_number:
        print(colored("\nNumber entered higher than generated number.", "green"))
        print(colored(f"\nNumber entered: {Guess}", "green"))
        Tries_left = Guesses - Tries
        print(colored(f"\nNumber of tries left: {Tries_left}", "green"))
    except ValueError:
      print(colored("\nInvalid input.", "red"))
      Easy()
  else:
    print(colored("\nYou lost.", "red"))
    print(colored(f"\nGenerated number: {Generated_number}", "green"))
    Display()

  
# Hard
def Hard():
  Generated_number =random2.randrange(0, 30)
  Guesses = 5
  Tries = 0
  print(colored("\nHard:\n-----", "blue"))
  while Tries < Guesses:
    try:
      Tries += 1
      Guess = int(input(colored("\nGuess: ", "blue")))
      if Guess == Generated_number:
        print(colored("\nYou won.", "red"))
        print(colored(f"\nNumber entered: {Guess}", "green"))
        print(colored(f"\nNumber of tries used: {Tries}", "green"))
        Display()
      elif Guess < Generated_number:
        print(colored("\nNumber entered lower than generated number.", "green"))
        print(colored(f"\nNumber entered: {Guess}", "green"))
        Tries_left = Guesses - Tries
        print(colored(f"\nNumber of tries left: {Tries_left}", "green"))
      elif Guess > Generated_number:
        print(colored("\nNumber entered higher than generated number.", "green"))
        print(colored(f"\nNumber entered: {Guess}", "green"))
        Tries_left = Guesses - Tries
        print(colored(f"\nNumber of tries left: {Tries_left}", "green"))
    except ValueError:
      print(colored("\nInvalid input.", "red"))
      Hard()
  else:
    print(colored("\nYou lost.", "red"))
    print(colored(f"\nGenerated number: {Generated_number}", "green"))
    Display()


Display()
