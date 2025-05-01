# Home Task 6: Rock-Paper-Scissor
import random
def playRockPaperScissor(rounds):
    a="rock"
    b="paper"
    c="scissor"
    user_score=0
    comp_score=0
    for i in range(rounds):
        user=input()
        X= random.choice([a, b, c])
        print(f"Computer: {X}")
        if (X==b and user==a) or (X==c and user==b):
            comp_score+=1
        elif (X==a and user==b) or (X==b and user==c):
            user_score+=1
    print(f"Your Score: {user_score}")
    print(f"Computer's Score: {comp_score}")
    if user_score>comp_score:
        print("You have won the game!")
    elif user_score<comp_score:
        print("Computer has won the game!")
playRockPaperScissor(int(input()))