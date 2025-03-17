import random

# List of words to guess
words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]  # Create a list of underscores ['_', '_', '_', '_', '_', '_']
attempts = 3  # Number of allowed attempts

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    print("\nTotal 3 Attempts")
    guess = input("Guess the Programming Language: ").lower()

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                if guess in word_display :
                    print('\nYou have already used that letter. Guess another letter.')
                else:
                    word_display[index] = guess # Reveal the letter
                
    else:
        print("That letter doesn't appear in the word.")
        attempts -= 1
        print(f"Attempts Left : {attempts}")

# Game conclusion
if '_' not in word_display:
    print("You guessed the Programming Language!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost!")