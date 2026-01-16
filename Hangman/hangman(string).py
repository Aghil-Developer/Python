import random
from hangman_words import word_list

from hangman_art import stages,logo

print(logo)
placeholder = ""

chosen_word = random.choice(word_list)
lengthOfWord = len(chosen_word)
lives = 6

for i in range(0,lengthOfWord):
    placeholder+="_"

print("Word to guess: "+ placeholder)

gameOver = False
correct_word = []
while not gameOver:
    print(f"\n****************************{lives} LIVES LEFT****************************")
    guessedWord = input("\nGuess a letter from the word: ")
    guessedWord = guessedWord.lower()

    display = ""
    for i in chosen_word:
        if guessedWord == i:
            display+=guessedWord
            correct_word.append(guessedWord)
        elif i in correct_word:
            display+=i
        else:
            display+="_"


    if guessedWord not in chosen_word:
        lives-=1
        print(f"Your guessed word: {guessedWord}, is not in the word , so you loose a life!!")
        if lives == 0:
            gameOver =True
            print("\n****************************YOU LOOSE****************************")

    if guessedWord in correct_word:
        print(f"You Have already guessed this word: {guessedWord}")

    print(display)

    if "_" not in display:
        gameOver=True
        print("\n****************************YOU WIN****************************")

    print(stages[lives])