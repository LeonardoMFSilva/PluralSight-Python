import random

computer_choice = random.choice(["scissors", "rock", "paper"])

user_choice = input("Choose: Rock, Paper, Scissors\n")

if computer_choice == user_choice:
    print("TIE! You chose: " + user_choice + " and the computer also chose: " + computer_choice)
elif user_choice == "rock" and computer_choice == "scissors":
    print("WIN! The computer chose: " + computer_choice + " and you chose: " + user_choice)
elif user_choice == "rock" and computer_choice == "scissors":
    print("WIN! The computer chose: " + computer_choice + " and you chose: " + user_choice)
elif user_choice == "rock" and computer_choice == "scissors":
    print("WIN! The computer chose: " + computer_choice + " and you chose: " + user_choice)
else:
    print("LOSE! You chose: " + user_choice + " and the computer chose: " + computer_choice)

