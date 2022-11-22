#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: November 22
# This program gets user's input and outputs the factorial


def fahrenheit():
    # This function receives data, calculates, then outputs

    # Asks the user for the temperature in celsius
    try:
        temperature_celsius = int(input("\nWhat is your temperature in celsius?: "))

    # Exception thrown if the user did not enter a number
    except ValueError:
        input("You must enter a positive integer. Please try again.")

    # Calculate the user's temperature to fahrenheit
    temperature_fahrenheit = temperature_celsius * 1.8 + 32

    # Display the results (temperature_fahrenheit) to the user
    print(f"\nYour temperature in fahrenheit is {temperature_fahrenheit} degrees")


def main():
    # This function calls the fahrenheit function

    # Call functions
    fahrenheit()


if __name__ == "__main__":
    main()
