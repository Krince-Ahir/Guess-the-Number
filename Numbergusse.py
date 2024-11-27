import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I have selected a random number between 1 and 10. Can you guess it?")
    
    # Generate a random number between 1 and 10050
    secret_number = random.randint(1, 100)
    
    attempts = 0
    
    while True:
        # Get user input for the guess
        user_guess = int(input("Enter your guess: "))
        
        # Increment the attempts counter
        attempts += 1
        
        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guess_the_number()
