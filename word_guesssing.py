import random

# Taking input for your name
name = input("What is your name? ")
print("Good Luck!", name)

words = ["computer", "mouse", "keyboard", "printer", "CPU"]
word = random.choice(words)

print("GUESS THE CHARACTERS")

guesses = ""
turns = 12

while turns > 0:
    failed = 0  # Count the number of user failures

    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        # User will win the game if failure is 0
        # and 'You Win' will be given as output
        print("\nYou Win")
        # This prints the correct word
        print("The word is:", word)
        break

    # If user has input the wrong alphabet then
    # it will ask the user to enter another alphabet
    print()
    guess = input("Guess a character: ")

    # Every input character will be stored in guesses
    guesses += guess

    # Check input with the character in the word
    if guess not in word:
        turns -= 1
        print("You have", turns, 'more guesses')

        if turns == 0:
            print("You Loose")
