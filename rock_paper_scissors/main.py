import random
def menu():
    while True:
        print("=========================","\n   Rock Paper Scissors","\n=========================")
        print("1)  ✊","\n2)  ✋","\n3)  ✌️")
        player = int(input("Pick a number: "))
        print()
        computer = random.randint(1,3)

        #if case para pedra
        if  player == 1 and computer == 1:
            print("You chose: ✊","\nCPU chose: ✊","\nIt is a draw!")
        elif player == 1 and computer == 2:
            print("You chose: ✊","\nCPU chose: ✋","\nThe CPU won!")
        elif player == 1 and computer == 3:
            print("You chose: ✊","\nCPU chose: ✌️","\nThe player won!")

        #if case para papel
        if player == 2 and computer == 2:
            print("You chose: ✋","\nCPU chose: ✋","\nIt is a draw!")
        elif player == 2 and computer == 3:
            print("You chose: ✋","\nCPU chose: ✌️","\nThe CPU won!")
        elif player == 2 and computer == 1:
            print("You chose: ✋","\nCPU chose: ✊","\nThe player won!")

        #if case para tesoura
        if player == 3 and computer == 3:
            print("You chose: ✌️","\nCPU chose: ✌️","\nIt is a draw!")
        elif player == 3 and computer == 1:
            print("You chose: ✌️","\nCPU chose: ✊","\nThe CPU won!")
        elif player == 3 and computer == 2:
            print("You chose: ✌️","\nCPU chose: ✋","\nThe player won!")
        
        print("\nTry again?", "\n1)Yes","\n2)No")
        play_again = int(input("type: "))
        if play_again == 1:
            continue
        else:
            print("Thanks for playing!")
            break

menu()
    

