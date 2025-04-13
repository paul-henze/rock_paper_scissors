import random
def menu():
    while True:
        print("=========================","\n   Rock Paper Scissors","\n=========================")
        print("1)  ✊","\n2)  ✋","\n3)  ✌️")
        #Made a While case here so everytime the input is not 1,2 or 3, a error message will appear
        while True:
            try:
                player = int(input("Pick a number: "))
                
                if player in [1,2,3]:
                    break
                else:
                    print("Wrong input. Please, Select the options between 1,2 or 3.")
            except ValueError:
                print("You should only type numbers.")

        print()
        computer = random.randint(1,3)       
        #if case for stone
        if  player == 1 and computer == 1:
            print("You chose: ✊","\nCPU chose: ✊","\nIt is a draw!")
        elif player == 1 and computer == 2:
            print("You chose: ✊","\nCPU chose: ✋","\nThe CPU won!")
        elif player == 1 and computer == 3:
            print("You chose: ✊","\nCPU chose: ✌️","\nThe player won!")

        #if case for paper
        if player == 2 and computer == 2:
            print("You chose: ✋","\nCPU chose: ✋","\nIt is a draw!")
        elif player == 2 and computer == 3:
            print("You chose: ✋","\nCPU chose: ✌️","\nThe CPU won!")
        elif player == 2 and computer == 1:
            print("You chose: ✋","\nCPU chose: ✊","\nThe player won!")

        #if case for scissor
        if player == 3 and computer == 3:
            print("You chose: ✌️","\nCPU chose: ✌️","\nIt is a draw!")
        elif player == 3 and computer == 1:
            print("You chose: ✌️","\nCPU chose: ✊","\nThe CPU won!")
        elif player == 3 and computer == 2:
            print("You chose: ✌️","\nCPU chose: ✋","\nThe player won!")

        print("\nTry again?", "\n1)Yes","\n2)No")
        #Made a While case here so everytime the input is not 1 or 2, a error message will appear
        while True:
            try:
                play_again = int(input("Type: "))
                if play_again in [1,2]:
                    break
                else:
                    print("Wrong input. Try the options 1 or 2.")
            except ValueError:
                print("Wrong input. Try the options 1 or 2.")
            
        if play_again == 1:
           continue
        else:
            print("Thanks for playing!")
            break
                

menu()
    

