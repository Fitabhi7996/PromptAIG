import random

def get_player_choice():
    choice = input("Enter your choice (rock/paper/scissors), or 'q' to quit: ").lower()
    while choice not in ['rock', 'paper', 'scissors', 'q']:
        choice = input("Invalid choice. Please enter rock, paper, scissors, or 'q' to quit: ").lower()
    return choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a draw!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    player_score = 0
    computer_score = 0
    draw_count = 0
    
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions:")
    print("Rock beats scissors. Scissors beats paper. Paper beats rock.")
    
    while True:
        print("------------------------------")
        player_choice = get_player_choice()
        
        if player_choice == 'q':
            break
        
        computer_choice = get_computer_choice()
        
        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        else:
            draw_count += 1
        
        print("Score:")
        print("You:", player_score)
        print("Computer:", computer_score)
        print("Draws:", draw_count)
        print("------------------------------")

play_game()
