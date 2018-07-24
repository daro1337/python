
#Rock-Paper-Scissors
player1 = (str(input("Player1: \n")))
player2 = (str(input("Player2: \n")))
choice1 =  (str(input("Player1: rock, paper or scissors?: \n")))
choice2 =  (str(input("Player2: rock, paper or scissors?: \n")))
while True:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
#ograniczamy input
    while choice1 not in ("rock", "paper", "scissors"):
        choice1 =  (str(input("Player1: rock, paper or scissors?: \n")))
    while choice2 not in ("rock", "paper", "scissors"):
     choice2 =  (str(input("Player2: rock, paper or scissors?: \n")))

    #print(choice1)
    #print(choice2)
    if choice1 == "rock" and choice2 == "scissors":
        print("Wygrywa " + player1)
        break
    elif choice1 == "rock" and choice2 == "paper":
        print("Wygrywa " + player2)
        break
    elif choice1 == "scissors" and choice2 == "paper":
        print("Wygrywa " + player1)
        break
    elif choice1 == "scissors" and choice2 == "rock":
        print("Wygrywa " + player2)
        break

    elif choice1 == "paper" and choice2 == "rock":
        print("Wygrywa " + player1)
        break
    elif choice1 == "paper" and choice2 == "scissors":
        print("Wygrywa " + player2)
        break

    else:
        print("REMIS :(")
        break
