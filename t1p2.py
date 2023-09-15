#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created Sept 13th 2023
# This program calculates a weighted average.

# calculates average weighting 20% for midterms and 40% for the final exam
def calculate_avg(first, second, third, final):
    weighted_avg = (first * 0.2) + (second * 0.2) + (third * 0.2) + (final * 0.4)
    print("")
    print(weighted_avg, "percent is your weighted average.")

# generic main function, gets input and runs calculate_avg()
def main():

    # intro and input
    print("\nWelcome to my weighted average calculator!\n")

    first_midterm = input("Enter your first midterm mark: ")
    second_midterm = input("Enter your second midterm mark: ")
    third_midterm = input("Enter your third midterm mark: ")
    final_exam = input ("Enter your final exam mark: ")

    # data validation thru float, then runs calculate_avg() function
    try:
        calculate_avg(
            float(first_midterm),
            float(second_midterm),
            float(third_midterm),
            float(final_exam)
        )
    except:
        print("\nPlease run again and ensure all inputs are numbers.")

    print("\nDone.")

if __name__ == "__main__":
    main()
