import random

options = ["Rock", "Paper", "Scissors"]
running = True

while running:
        
        player = None 
        computer = random.choice(options)
        
        while player not in options:
            player = input("Enter your choice (Rock,Paper,Scissors): ")
            print(f'Player: {player}')
            print(f'computer: {computer}')

        if player == computer:
                print("It's a tie!")
        elif player == "Rock" and computer == "Scissors":
                print("player wins!")
        elif player ==  "Paper" and computer == "Rock":
                print("player win!")
        elif player == "Scissors" and computer == "Paper":
                print("player win!")
        elif player == "Rock" and computer == "Paper":
                print("computer wins!")
        elif player == "Paper" and computer == "Scissors":
                print("Computer wins!")
        elif player == "Scissors" and computer == "Rock":
                print("computer wins!")
        else:
                print("You lose!")
                        
        # play_again = input("Do you want to play again? (y/n): ").lower()
        # if not play_again == "y":
        #                         running = False
            
        # print("Thanks for playing!")
