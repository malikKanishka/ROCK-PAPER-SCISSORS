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
    def rule(c1,c2):
        if c1==1 and c2==2:
            print(f"{player1} won!")
        elif c2==1 and c1==2:
            print(f"{player2} won!")
        elif c1==2 and c2==3:
            print(f"{player1} won!")
        elif c2==2 and c1==3:
            print(f"{player2} won!")
        elif c1==1 and c2==3:
            print(f"{player2} won!")
        elif c2==1 and c1==3:
            print(f"{player1} won!")
        else:
            if c1 not in [1,2,3] or c2 not in [1,2,3]:
                print("ENTER THE CORRECT CHOICE")
            else:
                print("It's a draw! As same choice.")
    while True:
        choice_1 = int(input("Enter your choice Player1=\n Press 1 for Rock\n Press 2 for Scissor\n Press 3 for Paper\nEnter here:-"))
        choice_2 = int(input("Enter your choice Player2=\n Press 1 for Rock\n Press 2 for Scissor\n Press 3 for Paper\nEnter here:-"))
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