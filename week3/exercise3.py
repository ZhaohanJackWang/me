"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def check_number(number):
  while True:
    try:
      number = int(number)
      return number
    except Exception:
      number = input("it is not number plz enter again: ")

def check_upper(upper, low):

  upper = check_number(upper)

  print(type(upper))


  while True:
    if upper > low:
      return upper
    else:
      upper = check_number(input("upper should bigger than low, plz enter again: "))


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    lowBound = input("Enter an low bound: ")
    lowBound = check_number(lowBound)

    upperBound = input("Enter an upper bound: ")
    upperBound = check_upper(upperBound, lowBound)


    actualNumber = random.randint(lowBound, upperBound)

    guessed = -1

    while guessed != actualNumber:
        guessedNumber = input("Guess a number: ")
        guessedNumber = check_number(guessedNumber)
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = actualNumber 
        elif guessedNumber > upperBound or guessedNumber < lowBound:
            print("outside of bounds")
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"


    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
