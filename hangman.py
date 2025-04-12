import random

ascii_art = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

with open("word_list.txt", "r") as f:
    word_list = [line.strip().lower() for line in f if len(line.strip()) > 3]


def game():
    while True:
        word = random.choice(word_list)
        if word not in used_words:
            used_words.add(word)
            break

    display = ["_" for _ in word]
    lives = 6
    letters = set()

    while lives > 0:
        print("\nWord to guess: " + " ".join(display))
        print("Guessed letters: " + ", ".join(letters))
        guess = input(f"You have {lives} lives left. Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in letters:
            print(f"You've already guessed {guess}.")
            continue

        letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    display[i] = guess
            print("Your guess is correct!")

            if display != list(word):
                print(f'The word is: {" ".join(display)}')
            else:
                print(f"\nYou guessed '{word.upper()}' correctly. YOU WIN!\n")
                score["wins"] += 1
                break
        else:
            print(
                "You guessed '" + guess + "', that's not in the word.\nYou lose a life."
            )
            lives -= 1
            print(ascii_art[6 - lives])

            if lives == 0:
                print(f"\nIt was '{word.upper()}'. YOU LOSE!\n")
                score["losses"] += 1
                break
    print("-" * 50)


print("Welcome to the Hangman Game!")
score = {"wins": 0, "losses": 0}
used_words = set()
try:
    continue_game = True
    while continue_game:
        game()
        print(f"\nCurrent Score -- Wins: {score['wins']} | Losses: {score['losses']}")
        choice = input("Want to play another round? (y/n) ").lower()
        continue_game = choice == "y"
except KeyboardInterrupt:
    print("\nGame interrupted. Thanks for playing!")

print("\nThanks for playing!")
