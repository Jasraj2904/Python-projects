import random

while True :
    user_action = input("Enter your choice (Rock, Paper and Scissors) : ")
    possible_actions = ["Rock" ,"Paper" , "Scissors"]
    computer_action = random.choice(possible_actions)
    print(f"You choose {user_action}, computer chose {computer_action}.")
    if user_action == computer_action:
        print("It's a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors" :
            print("Rock Smashes Scissors! You Win!")
        else:
            print("Paper covers rock! You Lose!")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers the rock! You Win!")
        else :
            print("Scissors cuts the Paper! You Lose!")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts paper! You Win!")
        else:
            print("Rock smashes scissors! You Lose!")
    play_again = input("Play Again? (y\n) : ")
    if play_again != "y":
        break