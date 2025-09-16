import random

possible_action = ("rock", "paper", "scissor")

#For count the score
user_score = 0
computer_score = 0
ties = 0

while True:
    user_action = input("Enter your choice (rock, paper, scissor): ").lower()
    computer_action = random.choice(possible_action)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        ties += 1
    elif user_action == "rock":
        if computer_action == "scissor":
            print("Rock smashes scissors! You win!")
            user_score += 1
        else:
            print("Paper covers rock! You lose.")
            computer_score += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_score += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_score += 1
    elif user_action == "scissor":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_score += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_score += 1
    else:
        print("Invalid choice! Please select rock, paper, or scissor.")

    # Show current scoreboard
    print(f"\nScoreboard: You = {user_score}, Computer = {computer_score}, Ties = {ties}\n")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("\nFinal Scoreboard:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        print(f"Ties: {ties}")
        print("Thanks for playing!")
        break
