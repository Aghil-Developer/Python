import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock,paper,scissors]

print("Welcome to Rock, Paper, Scissors!!")

userChoice = input("Enter your choice (Rock,Paper,Scissors): ")


if userChoice.lower() == "rock":
    userChoiceNumber = 0
elif userChoice.lower() == "paper":
    userChoiceNumber = 1
elif userChoice.lower() == "scissors":
    userChoiceNumber = 2

randomChoice = random.randint(0,2)

print("Computer Choice:\n")
print(choices[randomChoice])

print("Your Choice:\n")
print(choices[userChoiceNumber])


if randomChoice < userChoiceNumber and userChoiceNumber != 0:
    print("You Won!!")
elif userChoiceNumber == 0 and randomChoice == 2:
    print("You Won!!")
elif randomChoice == userChoiceNumber:
    print("Draw!!")
else:
    print("You Lost")

    