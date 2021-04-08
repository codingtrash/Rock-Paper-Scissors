#Author: Daniel Binns
#Date:02/03/2021
#Version 1.0
#Rock Paper Scissors game
#Two players

print("Welcome to Rock, Paper, Scissors!")
print("Let's begin...")
name1=input("Player 1: What's your name? \n")
name2=input("Player 2: What's your name? \n")

print("Hello " + name1 + " and " + name2)
print(name2 + " close your eyes!")

choice1 = input(name1 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ").lower()
print("Great choice! Now - cover your answer and ask " + name2 + " to choose. \n\n\n")
choice2 = input(name2 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ").lower()

#gameplay instances
if choice1 == "r" and choice2 == "p":
    print(name2 + " wins!")
   
if choice1 == "p" and choice2 == "r":
    print(name1 + " wins!")

if choice1 == "s" and choice2 == "p":
    print(name1 + " wins!")

if choice1 == "r" and choice2 == "r":
    print("Draw!")

if choice1 == "s" and choice2 == "s":
    print("Draw!")

if choice1 == "p" and choice2 == "p":
    print("Draw!")

if choice1 == "p" and choice2 == "s":
    print(name2 + " wins!")

if choice1 == "r" and choice2 == "s":
    print(name1 + " wins!")

if choice1 == "s" and choice2 == "r":
    print(name2 + " wins!")

print("Thanks for playing Rock Paper Scissors")