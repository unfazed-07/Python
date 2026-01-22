import random
options = ['rock', 'paper', 'scissor']
while (1):
    computer=random.choice(options)
    user=input("Enter your choice: Rock, Paper, Scissor").lower()
    print("Computer Choose: ", computer, "User Choose: ", user)
    if (user==computer):
        print("It's a Tie")
    elif (user=='rock' and computer=='scissor') or (user=='paper' and computer=='scissor') or (user == 'scissor' and computer == 'paper'): print("You Wins!🥳")
    else: print("Computer Wins")
