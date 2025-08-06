import random

word_list = ["car", "apple", "banana", "grape", "mango", "peach"]


chosen_word = random.choice(word_list)


display = ["_" for _ in chosen_word]


lives = 6
guessed_letters = []

print(" Welcome to Hangman!")
print("Guess the word by entering one letter at a time.")


while lives > 0 and "_" in display:
    print("\nCurrent word:", " ".join(display))
    guess = input("Enter a letter: ").lower()


    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter. Try another.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print(" Good guess!")

        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
    else:
        lives -= 1
        print(f" Wrong guess! You have {lives} lives left.")


if "_" not in display:
    print("\n Congratulations! You guessed the word:", chosen_word)
else:
    print("\n Game Over! The correct word was:", chosen_word)

