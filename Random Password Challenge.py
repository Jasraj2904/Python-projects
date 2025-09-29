import random
import string

def generate_password(length=6):
    """Generate a password with at least one lowercase, uppercase, and digit."""
    if length < 3:
        raise ValueError("Length must be at least 3 to include required character types.")
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    # Ensure at least one of each required type
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    all_chars = lowercase + uppercase + digits
    password_chars += random.choices(all_chars, k=length - 3)

    random.shuffle(password_chars)
    return ''.join(password_chars)

def compare_guess(secret, guess):
    """
    Returns (correct_pos, correct_char_wrong_pos).
    - correct_pos: number of characters matching in exact position.
    - correct_char_wrong_pos: number of characters present in secret but in wrong position.
    """
    # Correct positions
    correct_pos = sum(s == g for s, g in zip(secret, guess))

    # For counting characters present but wrong position:
    # Count occurrences of each char in secret and guess, then subtract correctly positioned matches.
    from collections import Counter
    secret_counter = Counter(secret)
    guess_counter = Counter(guess)

    # Count total correct characters disregarding position
    total_correct_chars = sum((secret_counter & guess_counter).values())

    correct_wrong_pos = total_correct_chars - correct_pos
    return correct_pos, correct_wrong_pos

def play_game():
    print("Welcome to 'Guess the Password' game!")
    while True:
        try:
            length = int(input("Choose password length (recommended 6-10): ").strip() or "6")
        except ValueError:
            print("Please enter a valid integer for length.")
            continue
        if length < 3:
            print("Please choose a length of at least 3.")
            continue
        break

    secret = generate_password(length)
    max_attempts = length * 3  # arbitrary attempt limit; you can change this
    attempts = 0

    print("\nA password has been generated using:")
    print("- lowercase letters (a-z)")
    print("- uppercase letters (A-Z)")
    print("- digits (0-9)")
    print(f"The password length is: {length}")
    print(f"You have {max_attempts} attempts to guess it. Type 'quit' to give up.\n")

    # Uncomment the next line for debugging to see the secret:
    # print("DEBUG: secret password is:", secret)

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess: ").strip()
        if guess.lower() == 'quit':
            print(f"You gave up. The password was: {secret}")
            break
        if len(guess) != length:
            print(f"Your guess must be exactly {length} characters long. Try again.")
            continue

        attempts += 1
        if guess == secret:
            print(f"🎉 Correct! You've guessed the password in {attempts} attempts.")
            break

        correct_pos, correct_wrong_pos = compare_guess(secret, guess)
        print(f"Hints: {correct_pos} character(s) correct and in the right position; "
              f"{correct_wrong_pos} correct but in the wrong position.\n")
    else:
        # executed if loop not broken (i.e., attempts exhausted)
        print(f"Out of attempts! The password was: {secret}")

    # Play again?
    again = input("Play again? (y/n): ").strip().lower()
    if again == 'y':
        print("\n" + "="*40 + "\n")
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    play_game()