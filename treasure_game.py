print("Welcom to treasure hunt!!!")
print("The only rule is to choose blindly among the choices!")
print("\nChoose your options wisely!!\n")
print("\nYour journey starts here!")


print("\nYour reached the port,do you need to \"WAIT FOR BOAT\" or \"SWIM\" to the island??")
question1 = input("\nType \"WAIT\" or \"SWIM\": ")

if question1.lower()=="swim":
    print("\nSince you can't swim in the water for too long you ,are drowned to death 😔")

else:
    print("\nNow you have reached the Island, there are two ways \"LEFT\" & \"RIGHT\"")
    question2 = input("\nType \"LEFT\" or \"RIGHT\": ")

    if question2.lower() == "left":
        print("\nSince you chose a wrong route, you fell from a big cliff and you are dead 😔")
    else:
        print("\nYou have entered a cave, now you need to choose a door among 3 doors blindly")
        question3 = input("\nType \"1\" for door 1, \"2\" for door 2, \"3\" for door 3: ")
        if question3.lower() == "3":
            print("\nSince you entered a wrong door, you entered a door with poisonous gas place and you are dead 😔")
        elif  question3.lower() == "1":
            print("\nSince you entered a wrong door, you entered a door full of deadly bees ,so you were stung to death 😔")
        else:
            print("\nSince you have finally reached the treasure!!!")
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
