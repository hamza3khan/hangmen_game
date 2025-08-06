 Hangman Game (Console Version)

 Project Description

This is a simple **text-based Hangman game written in Python**.  
The game randomly selects a word from a predefined list, and the player has to guess it one letter at a time.  
The player gets **6 chances (lives)** before the game ends.

---

 Key Concepts Used

- `random` module
- `while` loops
- `if-else` conditions
- `strings` and `lists`
- `input()` and `print()` functions

---

Features

- Random word selection from a fixed list of 5 words.
- User guesses letters one at a time.
- Tracks guessed letters and prevents repeated inputs.
- Displays progress after each guess.
- Allows only 6 incorrect guesses.
- Displays win or lose message at the end.



 How to Run

1. Save the code into a file called `hangman.py`.
2. Make sure you have Python installed.
3. Run it from the terminal or command prompt:

python hangman.py


Main Purpose of the Hangman Game
The main purpose of the Hangman game is:

To help players improve their word-guessing and problem-solving skills in a fun and interactive way
In a Programming Context (Python Project):
If you're building it as a coding project, then the purpose is also educational:

Practice Python basics:

loops, if-else, strings, lists, random, input/output

 Learn how to handle user input and build a game loop.

 Understand logic building — how to check guesses, track state, and give feedback.
 For the Player:
Build vocabulary and spelling skills.

Improve thinking under pressure (only 6 chances).

Have fun with a simple, text-based word puzzle game.



OUTPUT

 Welcome to Hangman!
Guess the word by entering one letter at a time.

Current word: _ _ _ _ _
Enter a letter: a
 Good guess!

Current word: a _ _ _ e
Enter a letter: z
Wrong guess! You have 5 lives left.

...
 Congratulations! You guessed the word: apple

