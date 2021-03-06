import random

name = input("Enter your name: ")
print(f"Hello My Friend {name}")
print("Let's play rock-paper-scissor")
print("You will have 3 tries")
print("The person that has most wins at then end wins")
tries = 3
computerPoints = 0
playerPoints = 0

def evaluate():
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        return "rock"
    if randomNumber == 2:
        return "paper"
    if randomNumber == 3:
        return "scissor"

def points(case):
    global computerPoints
    global playerPoints
    if case == 1:
        playerPoints += 1
        print("ahhh... You won")
        print(f"Computer Points: {computerPoints}")
        print(f"Your Points: {playerPoints}")
    if case == 2:
        computerPoints += 1
        print("Yes... I won")
        print(f"Computer Points: {computerPoints}")
        print(f"Your Points: {playerPoints}")

def show(evaluate):
    print(f"You: {move}")
    print(f"Computer: {evaluate}")

while tries >= 0:
    print(f"You have {tries} left")
    print("                      ")
    print("Choose the respective move: ")
    print("rock: 1")
    print("paper: 2")
    print("scissor: 3")

    move = int(input(": "))

    evaluate1 = evaluate()

    if  evaluate1 == "rock" and move == 2:
        show(evaluate1)
        points(1)
    if evaluate1 == "paper" and move == 3:
        show(evaluate1)
        points(1)
    if evaluate1 == "scissor" and move == 1:
        show(evaluate1)
        points(1)
    if evaluate1 == "scissor" and move == 2:
        show(evaluate1)
        points(2)
    if evaluate1 == "paper" and move == 1:
        show(evaluate1)
        points(2)
    if evaluate1 == "rock" and move == 3:
        show(evaluate1)
        points(2)
    


    tries = tries - 1



winnner = None

if computerPoints > playerPoints:
    winnner = "Computer"
if playerPoints > computerPoints:
    winner = "Player"


print(f"The Winner is : {name}")