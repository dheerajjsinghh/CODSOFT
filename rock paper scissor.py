import random  #importing random library

def ropasi():   #defining a function for game
    user_win,comp_win=0,0

    choice=["Rock","Paper","Scissor"]

    result_list = [["Tie", "Lose", "Win"], ["Win", "Tie", "Lose"], ["Lose", "Win", "Tie"]]

    for x in range(5):
        user_input=int(input("Enter your choice---\n0 for Rock\n1 for Paper\n2 for Scissor\n"))
        comp_input=random.randint(0,2)
        print(f"Your input is: {choice[user_input]}")
        print(f"Computer input is: {choice[comp_input]}")

        result="~~~"+result_list[user_input][comp_input]+"~~~"
        print(result)

        if result=="Win":
            user_win+=1
        elif result=="Lose":
            comp_win+=1

    if user_win>comp_win:
        print("You Won the Game")
    elif user_win<comp_win:
        print("Computer Won the Game")
    else:
        print("Game Tied")

    i="Yes"
    while (i=="Yes"):
        i=input("Do you want to play again (Yes/No): ")

        if i=="Yes" or i=="yes" or i=="YES":
            ropasi()      #recursive function , if user wants to play again
        else:
            print("---Thankyou for playing the game---")
            break

ropasi()     #calling function