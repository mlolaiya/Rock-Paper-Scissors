import random

computer_wins = 0
player_wins = 0

def SelectOption ():
    user_option = input("choose Rock, Paper or Scissors: ")
    if user_option in ["Rock", "rock", "r", "R"]:
        user_option = "r"
    elif user_option in ["Paper", "paper", "p", "P"]:
        user_option = "p"
    elif user_option in ["Scissors", "scissors", "s", "S"]:
        user_option = "s"
    else:
        print("Wrong input, Retry.")
        SelectOption()
    return user_option

def ComputerOption():
    comp_option = random.randint(1,3)
    if comp_option == 1:
        comp_option = "r"
    elif comp_option == 2:
        comp_option = "p"
    else:
        comp_option = "s"
    return comp_option

while True:
    print("")
    user_option = SelectOption()
    comp_option = ComputerOption()
    print("")

    if user_option == "r":
        if comp_option == "r":
            print("You both chose rock. You tied.")
        elif comp_option == "p":
            print("Computer wins.")
            computer_wins += 1

        elif comp_option == "s":
            print("you chose rock. The computer choose scissors. you win.")
            player_wins += 1

    elif user_option == "p":
        if comp_option == "r":
            print("You chose paper. The computer chose rock. you win.")
            player_wins += 1

    elif user_option == "p":
        if comp_option == "r":
            print("You chose paper. The Computer chose rock. you win.")
            player_wins += 1
        elif comp_option == "p":
            print("You both chose paper. you tied")

        elif comp_option == "s":
            print("you chose paper. The computer chose scissors. you lose.")
            computer_wins += 1
    elif user_option == "s":
        if comp_option == "r":
            print("You chose scissors, the computer chose rock. You lose.")
            computer_wins += 1
        elif comp_option== "p":
            print("You choose scissors, the computer choose paper. you win.")
            player_wins += 1
        elif comp_option == "s":
            print("You chose scissors. The computer chose scissors. You tied.")

    print("")
    print("Player wins: " + str(player_wins))
    print("computer wins: " + str(computer_wins))
    print("")

    user_option = input("Do you want to play again? (y/n)")
    if user_option in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_option in ["N", "n", "no", "No"]:
        break
    else:
        break








