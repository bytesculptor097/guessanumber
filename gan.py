# Importing the random number generator library
import random as r

# Initializing random numbers for different levels
rande = r.randint(1, 50)
randm = r.randint(1, 100)
randh = r.randint(1, 500)

# Function to handle the guessing game
def guess_num():
    global rande, randm, randh
    # Displaying the welcome message and game instructions
    print("\t\t-----Welcome to the Guessing Game!------")
    print("You have three levels to play:")
    print("1. Easy (1-50)")   
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")
    level = input("Choose your level (easy/medium/hard): ").lower()
    # Validating the level input if 'easy'
    if level == "easy":
        print("Guess a number between 1 and 50")
        guess = int(input("Enter your guess: "))

        if guess == rande:
            print("Congratulations! You guessed the number correctly.")
        elif guess < rande:
            print("Your guess is lower than the number. The number was", rande )
            print("Better luck next time!")
        else:
            print("Your guess is higher than the number. The number was", rande )
            print("Better luck next time!")
    # Validating the level input if 'medium'
    elif level == "medium":
        print("Guess a number between 1 and 100")
        guess = int(input("Enter your guess: "))

        if guess == randm:
            print("Congratulations! You guessed the number correctly.")
        elif guess < randm:
            print("Your guess is lower than the number. The number was", randm )
            print("\nBetter luck next time!")
        else:
            print("Your guess is higher than the number. The number was", randm )
            print("\nBetter luck next time!")
    # Validating the level input if 'hard'
    elif level == "hard":
        print("Guess a number between 1 and 500")
        guess = int(input("Enter your guess: "))

        if guess == randh:
            print("Congratulations! You guessed the number correctly.")
        elif guess < randh:
            print("Your guess is lower than the number. The number was", randh )
            print("Better luck next time!")
        else:
            print("Your guess is higher than the number. The number was", randh )
            print("Better luck next time!")
    else:
        print("Invalid level. Please choose either 'easy', 'medium', or 'hard'.")
        
# Calling the function to start the game
guess_num()
