# [2015-11-02] Challenge #239 [Easy] A Game of Threes

# Background
# Back in middle school, I had a peculiar way of dealing with super boring classes. I would take my handy pocket calculator and play a "Game of Threes". Here's how you play it:
#
# First, you mash in a random large number to start with. Then, repeatedly do the following:
#
# If the number is divisible by 3, divide it by 3.
# If it's not, either add 1 or subtract 1 (to make it divisible by 3), then divide it by 3.
# The game stops when you reach "1".
#
# While the game was originally a race against myself in order to hone quick math reflexes, it also poses an opportunity for some interesting programming challenges. Today, the challenge is to create a program that "plays" the Game of Threes.
#
# Challenge Description
# The input is a single number: the number at which the game starts. Write a program that plays the Threes game, and outputs a valid sequence of steps you need to take to get to 1. Each step should be output as the number you start at, followed by either -1 or 1 (if you are adding/subtracting 1 before dividing), or 0 (if you are just dividing). The last line should simply be 1.
#
# Input Description
# The input is a single number: the number at which the game starts.
#
# 100
# Output Description
# The output is a list of valid steps that must be taken to play the game. Each step is represented by the number you start at, followed by either -1 or 1 (if you are adding/subtracting 1 before dividing), or 0 (if you are just dividing). The last line should simply be 1.
#
# 100 -1
# 33 0
# 11 1
# 4 -1
# 1
# Challenge Input
# 31337357

def solve(input):
    while input != 1:
        step = 0
        if input % 3 == 1:
            step = -1
        elif input % 3 == 2:
            step = 1
        print(str(input) + " " + str(step))
        input = int((input + step)/3)
    print(input)

# simplified python solution from reddit
def alternative(input):
    while input != 1:
        # treat (0, -1, 1) as a list where the modulo of input is the index of that list to retrieve one of the values
        print("%d %d" % (input, (0, -1, 1)[int(input % 3)]))
        input = (input + (0, -1, 1)[int(input % 3)]) / 3

solve(31337357)
