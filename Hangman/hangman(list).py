import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
placeholder = []
lives = len(stages)-1
chosen_word = random.choice(word_list)
print(chosen_word)
lengthOfWord = len(chosen_word)

for i in range(0,lengthOfWord):
    placeholder.append("_")
print("Word to guess: ", *placeholder)


gameOver = False
while not gameOver:
    print(f"\n****************************{lives} LIVES LEFT****************************")
    guessedWord = input("\nGuess a letter from the word: ")
    guessedWord = guessedWord.lower()

    x=0
    for i in chosen_word:
        if guessedWord == i:
            placeholder[x] = guessedWord
        x+=1
    
    if guessedWord not in chosen_word:
        lives-=1
        print(f"Your guessed word: {guessedWord}, is not in the word , so you loose a life!!")
        if lives == 0:
            gameOver = True
            print("\n****************************YOU LOOSE****************************")

    if guessedWord in placeholder:
        print(f"You have already guessed the word: {guessedWord}")


    print(*placeholder)

    if "_" not in placeholder:
        gameOver=True
        print("\n****************************YOU WIN****************************")


    print(stages[lives])