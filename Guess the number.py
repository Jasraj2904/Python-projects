import random

def guess_the_number():
    print("Welcome to Guess the Number Game! 🎲")
    number = random.randint(1, 100)  # Computer chooses a number
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            
            if guess < number:
                print("Too low! 📉 Try again.")
            elif guess > number:
                print("Too high! 📈 Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number!")

# Run the game
guess_the_number()