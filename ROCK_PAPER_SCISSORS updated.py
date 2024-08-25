#Importing Random LIB
import random
#DEF FOR AGAINST COMPUTER
def against_computer():
    player = input("Player: ENTER YOUR NAME=\n") #ENTER THE NAME
    def selection():
        list_ = ["Rock", "Paper", "Scissor"]
        return random.choice(list_) #RANDOM CHOICE

    def rule(player_choice, computer_choice): #MAIN RULE SEC OF THE GAME
        if player_choice == 1 and computer_choice == "Scissor":
            print(f"Player:{player}, you won!\nAs Computer selected {computer_choice}\n")
        elif player_choice == 1 and computer_choice == "Paper":
            print(f"Computer won!\nAs Computer selected {computer_choice}\n\n")
        elif player_choice == 2 and computer_choice == "Paper":
            print(f"Player: {player}, you won!\nAs Computer selected {computer_choice}\n")
        elif player_choice == 2 and computer_choice == "Rock":
            print(f"Computer won!\nAs Computer selected {computer_choice}\n")
        elif player_choice == 3 and computer_choice == "Rock":
            print(f"Player: {player}, you won!\nAs Computer selected {computer_choice}\n")
        elif player_choice == 3 and computer_choice == "Scissor":
            print(f"Computer won!\nAs Computer selected {computer_choice}\n")
        else:
            if player_choice not in [1,2,3]:
                print("Please Enter the correct choice.")
            else:
                print(f"It's a draw! Both selected {computer_choice}\n")

    while True: #LOOP AND STOPPING CONDITION 
        choice = int(input("Enter your choice=\n Press 1 for Rock\n Press 2 for Scissor\n Press 3 for Paper\n\nEnter here:-"))
        computer_choice = selection()
        rule(choice, computer_choice) 
        continue_ = input("Enter '/' to play again or any other key to exit: ")
        if continue_ != '/':
            print("Game Over")
            break

#DEF FOR AGAINST FRIEND

def against_friend():
    player1=input("Player1: Input your name=\n")
    player2=input("Player2: Input your name=\n")
    print(f"\nPlayer1:{player1}\nPlayer2:{player2}\nWelcome to the game!\n")
    def rule(player1_choice, player2_choice): #MAIN RULE SEC OF THE GAME
        if player1_choice == "Rock" and player2_choice == "Scissor":
            print(f"Player:{player1}, you won!\nAs you selected {player1_choice} and {player2} selected {player2_choice}")
        elif player1_choice == "Rock" and player2_choice == "Paper":
            print(f"Player:{player2}, you won!\nAs you selected {player2_choice} and {player1} selected {player1_choice}\n")
        elif player1_choice == "Scissors" and player2_choice == "Paper":
            print(f"Player: {player1}, you won!\nAs you selected {player1_choice} and {player2} selected {player2_choice}")
        elif player1_choice == "Scissors" and player2_choice == "Rock":
            print(f"Player:{player2}, you won!\nAs you selected {player2_choice} and {player1} selected {player1_choice}")
        elif player1_choice == "Paper" and player2_choice == "Rock":
            print(f"Player: {player1}, you won!\nAs you selected {player1_choice} and {player2} selected {player2_choice}")
        elif player1_choice == "Paper" and player2_choice == "Scissor":
            print(f"Player:{player2}, you won!\nAs you selected {player2_choice} and {player1} selected {player1_choice}\n")
        else:
            print(f"It's a draw! Both selected {player1_choice}\n")

    def selection():
        selection=["Rock","Paper","Scissors"]
        return random.choice(selection)
    
    while True:
        choice_1 = selection()
        choice_2 = selection()
        rule(choice_1,choice_2)
        
        continue_ = input("\nEnter '/' to play again or any other key to exit: ")
        if continue_ != '/':
            print("Game Over")
            break


#MAIN  
type=int(input("ENTER WHETHER YOU WANT TO PLAY WITH A FRIEND OR COMPUTER\n PRESS 9 FOR AGAINST COMPUTER\n PRESS 5 FOR AGAINST FRIEND\nENTER HERE:="))
if type==9:
    against_computer()
elif type==5:
    against_friend()
else:
    print("Enter a valid choice!")
#END OF CODE