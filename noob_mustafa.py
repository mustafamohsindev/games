import random

# Function to generate a random number between a specified range
def generate_random_number(start, end):
    return random.randint(start, end)

# Main function for the game
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I've selected a number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    secret_number = generate_random_number(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    # Main game loop
    while True:
        # Get the player's guess
        # Increment the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        # if guess == secret_number:
#  print("Congratulations! You've guessed the number in", attempts, "attempts.")break
        # elif guess < secret_number:#         guess = int(input("Enter your guess: "))
        

            # print("Too low! Try guessing a higher number.")
        # else:
            # print("Too high! Try guessing a lower number.")

# Call the main function to start the game
number_guessing_game()