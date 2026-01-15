import random

names = []
numberOfPeople  = int(input("Enter the number of people: "))

for i in range(numberOfPeople):
    name = input(f"Enter name of person {i+1}: ")
    names.append(name)

rand = random.randint(0,numberOfPeople-1)

print(f"The bill payer choosen is {names[rand]}")