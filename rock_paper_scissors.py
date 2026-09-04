import random
print("----- ROCK PAPER SCISSORS GAME -----")
choices = ["rock", "paper", "scissors"]
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
computer_choice = random.choice(choices)
print("Your choice:", user_choice)
print("Computer choice:", computer_choice)
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
else:
    print("You lose!")