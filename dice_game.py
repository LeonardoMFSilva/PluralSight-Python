import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    p1 = input("P1, enter your name: ")
    p2 = input("P2, enter your name: ")

    roll1 = roll_dice();
    roll2 = roll_dice();

    print(p1, "rolled:", roll1)
    print(p2, "rolled:", roll2)

    if roll1 > roll2:
        print(p1, "wins!")
    elif roll2 > roll1:    
        print(p2, "wins!")
    else:
        print("Tie!")

main()