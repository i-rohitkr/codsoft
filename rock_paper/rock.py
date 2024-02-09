import random

def play_round():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print("Choose: rock, paper, or scissors")
    user_choice = input().lower()

    if user_choice in choices:
        print(f"Computer chose {computer_choice}")

        if user_choice == computer_choice:
            return 'It\'s a tie!', 0
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            return 'You win!', 1
        else:
            return 'You lose!', -1
    else:
        return 'Invalid choice. Please choose rock, paper, or scissors.', 0

def play_game():
    score = 0
    rounds = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        print("\nCurrent Score: You -", score, "| Computer -", rounds - score)
        result, points = play_round()
        print(result)

        score += points
        rounds += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final Score: You -", score, "| Computer -", rounds - score)
        else:
            print("please choose valid choice:")    
            break

if __name__ == "__main__":
    play_game()