import random

def dice_rolling_simulator():
    roll_again = "yes"
    
    while roll_again.lower() == "yes" or roll_again.lower() == "y":
        print("Rolling the dice...")
        print("Result: ", random.randint(1, 6))
        
        roll_again = input("Roll the dice again? (yes/no): ")

if __name__ == "__main__":
    dice_rolling_simulator()
