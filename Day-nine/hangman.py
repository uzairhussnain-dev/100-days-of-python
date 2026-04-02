import random

words = ["python", "javascript", "crypto", "developer", "blockchain"]

def hangman():
    word = random.choice(words)
    guessed = []
    attempts = 6

    print("🎮 Welcome to Hangman!")

    while attempts > 0:
        display = ""

        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)

        if "_" not in display:
            print("🎉 You guessed the word!")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("⚠️ Already guessed")
            continue

        guessed.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"❌ Wrong! Attempts left: {attempts}")

    if attempts == 0:
        print(f"💀 You lost! Word was: {word}")

hangman()