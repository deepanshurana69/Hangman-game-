import random

WORDS = ["python", "computer", "programming", "developer", "algorithm"]
MAX_INCORRECT_GUESSES = 6


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_game():
    word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0

    print("\n=== CodeAlpha Hangman Game ===")
    print("Guess the hidden word one letter at a time.")
    print(f"You can make {MAX_INCORRECT_GUESSES} incorrect guesses.\n")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("Word:", display_word(word, guessed_letters))
        print("Incorrect guesses:", incorrect_guesses)
        if guessed_letters:
            print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Enter a single letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!\n")
        else:
            incorrect_guesses += 1
            print("Incorrect guess!\n")

        if all(letter in guessed_letters for letter in word):
            print("Word:", display_word(word, guessed_letters))
            print(f"Congratulations! You guessed the word: {word}")
            return

    print(f"Game over! The word was: {word}")


if __name__ == "__main__":
    play_game()
