# A Robot moves in a Plane starting from the origin point (0,0).
# The robot can move UP, DOWN, LEFT, and RIGHT.
# The trace of Robot movement is as given following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# (The numbers after directions are steps)
# Write a program to compute the current distance from the origin point after sequencing of movements.
#
# Hint:Use the math module.

steps = "UP 5 DOWN 3 LEFT 3 RIGHT 2"
steps = steps.split(" ")
directions = steps[::2]
steps = steps[1::2]

distance = 0

for direction,step in zip(directions,steps) :
    step = int(step)
    match direction:
        case "UP":
            distance += step
        case "DOWN":
            distance -= step
        case "LEFT":
            distance -= step
        case "RIGHT":
            distance += step
        case _:
            print("Invalid Direction")
            exit()
print(f"current distance : {distance}")