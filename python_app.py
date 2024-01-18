# Import Random
# Define a function to rol the dice
# Create a dictionary that will have the drowings of the dice

import random

def roll_dice():
    dice_drowings = {
        1:(
                 " -------",
                "|   2   |",
                "|   •   |",
                "|       |",
                " -------",
        ),
        2:(
                 " -------",
                "| •     |",
                "|   2   |",
                "|     • |",
                 " -------",
        ),
        3:(
                 " -------",
                "| •  3  |",
                "|   •   |",
                "|     • |",
                 " -------",
        ),
        4:(
                 " -------",
                "| •   • |",
                "|   4   |",
                "| •   • |",
                 " -------",
        ),
        5:(
                 " -------",
                "| • 5 • |",
                "|   •   |",
                "| •   • |",
                 " -------",
        ),
        6:(
                 " -------",
                "| •   • |",
                "| • 6 • |",
                "| •   • |",
                 " -------",
        )
    }
    roll = input("Rolling dice (Yes/No): ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)


        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drowings[dice1]))
        print("\n".join(dice_drowings[dice2]))

        roll = input("Roll again? (Yes/No): ")

roll_dice()