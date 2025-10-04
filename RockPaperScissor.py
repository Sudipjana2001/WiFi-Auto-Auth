import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    user = input("Enter rock, paper, or scissors: ").lower()
    if user == computer:
        print(f"computer choose {computer}")
        print("Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print(f"computer choose {computer}")
        print("You win!")
    else:
        print(f"computer choose {computer}")
        print("Computer wins!")

play_game()


