import random

def main():
    # Generate the secret number at random
    secret_number: int = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")

    # Initialize user's guess
    guess = -1  # Start with an invalid guess
    
    # Loop until the guess matches the secret number
    while guess != secret_number:
        # Get user's guess
        guess = int(input("Enter a guess: "))
        
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
    
    # Congratulate the user upon guessing correctly
    print("Congrats! The number was: " + str(secret_number))

if __name__ == '__main__':
    main()
