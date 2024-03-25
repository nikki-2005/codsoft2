import random

def play_again():
  """Asks the user if they want to play another round."""
  choice = input("Do you want to play again? (y/n): ").lower()
  return choice == 'y'

def determine_winner(user_choice, computer_choice):
  """Determines the winner based on user and computer choices."""
  # Tie condition
  if user_choice == computer_choice:
    return "Tie"
  
  # Winning conditions
  if user_choice == "rock":
    if computer_choice == "scissors":
      return "Win"
    else:
      return "Lose"
  elif user_choice == "paper":
    if computer_choice == "rock":
      return "Win"
    else:
      return "Lose"
  elif user_choice == "scissors":
    if computer_choice == "paper":
      return "Win"
    else:
      return "Lose"
  else:
    return "Invalid Input"  # Handle unexpected user input

def main():
  """Main function to run the game."""
  score_user = 0
  score_computer = 0
  
  while True:
    print("\nRock Paper Scissors!")

    # User input
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    valid_choices = ["rock", "paper", "scissors"]
    while user_choice not in valid_choices:
      user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()

    # Computer selection
    computer_choice = random.choice(valid_choices)

    # Display choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner and update scores
    result = determine_winner(user_choice, computer_choice)
    if result == "Win":
      score_user += 1
      print("You win!")
    elif result == "Lose":
      score_computer += 1
      print("You lose!")
    else:
      print("It's a tie!")

    # Print scores
    print(f"\nYour score: {score_user}")
    print(f"Computer score: {score_computer}")

    # Play again prompt
    if not play_again():
      break

  print("\nThanks for playing!")

if __name__ == "__main__":
  main()
