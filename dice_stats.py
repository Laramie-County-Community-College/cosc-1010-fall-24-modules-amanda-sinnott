'''
Objective:

In this assignment, you will create two Python programs: a module dice_roller.py and a main program roll_stats.py. This will test your understanding of functions, modules, user input, and data analysis.

Part 1: dice_roller.py

Create a new file named dice_roller.py.
Define a function called roll_die(sides) that takes an integer sides representing the number of sides on a die (minimum 4).
Inside the function:
Check if sides is less than 4. If so, raise a ValueError with an appropriate message.
Use random.randint(1, sides) to roll the die and return the result.

Write unit tests:
Examine the supplied testing function called test_dice_roller().
This function loops to roll a D6 (6 sides) and a D10 (10 sides) 100 times each.
It uses assert to throw an error if all rolls for each die are not within valid ranges (1 to 6 for D6, 1 to 10 for D10).

Run the module:
Make sure you have random imported in your module.
Run dice_roller.py directly. The unit tests should run and indicate success.

Part 2: dice_stats.py

Inside the file named dice_stats.py.
Import the dice_roller module.
Define a function called main():
Prompt the user to enter the number of dice rolls and the number of sides on the die.
Use the supplied dictionary to store roll counts for each side (initialize with 0 for each side).
Use a loop to roll the die (using dice_roller.roll_die) the specified number of times.
Increment the count for the rolled side in the dictionary.
Iterate through the dictionary and calculate the probability of each side appearing, expressed as a percentage.
Print a formatted table showing the side, number of rolls, and probability for each side.
Run the program:
Make sure you have both dice_roller.py and dice_stats.py in the same directory.
Run dice_stats.py. The program should prompt for input, roll the dice, and display the statistics.
'''

import dice_roller

def main():
    num_rolls = int(input("Enter the number of dice rolls: "))
    sides = int(input("Enter the number of sides on the die: "))

    roll_counts = {side: 0 for side in range(1, sides + 1)}

    for _ in range(num_rolls):
        roll = dice_roller.roll_die(sides)
        roll_counts[roll] += 1
    
    print("\nSide\tRolls\tProbability (%)")
    for side, count in roll_counts.items():
        probability = (count / num_rolls) * 100
        print(f"{side}\t{count}\t{probability: .2f}")

if __name__ == "__main__":
    main()


def main():
    """Calculates and displays statistics from multiple dice rolls."""

    num_rolls = int(input("Enter the number of dice rolls: "))
    num_sides = 6

    roll_counts = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}  # Initialize roll count dictionary

    #Use a loop to roll the die (using dice_roller.roll_die) the specified number of times.
    #Increment the count for the rolled side in the dictionary.

    #Print a formatted table showing the side, number of rolls, and probability for each side.

if __name__ == "__main__":
    main()
