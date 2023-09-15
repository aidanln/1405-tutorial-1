#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales and Jonathan Pasco-Arnone
# Created Sept 13th 2023
# This program determines if a car can go through an intersection.

# decides if a car can go through an intersection and prints
def intersection(light_color, time_to_intersection):
    if light_color == "green":
        print("\nYour car can go.")
    elif light_color == "yellow" and time_to_intersection <= 5:
        print("\nYour car can go.")
    elif light_color == "red" and time_to_intersection <= 2:
        print("\nYour car can go.")
    else:
        print("\nSTOP! Your car cannot go.")

# stereotypical main function, gets input and runs thru intersection()
def main():

    # intro and input
    print("\nShould you go through an intersection?\n")
    light_color = input("What color is the light? ")
    distance = input("How far (in m) are you from the intersection? ")
    speed = input("How fast (in m/s) are you going? ")

    # data validation and intersection() function
    try:
        time_to_intersection = float(distance) / float(speed)
        intersection(light_color, time_to_intersection)
    except:
        print("\nError, make sure distance and speed are numbers.")

    print("\nDone.")

if __name__ == "__main__":
    main()
