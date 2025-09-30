#!/usr/bin/env python3

# Created By: Brandon
# Date: September 30th, 2025
# This program asks the user for the diameter of a pizza, calculates the total cost
# then displays the final price of the pizza

import constants


# Takes input from user
def main():
    diameter = int(input("Enter Diameter of the Pizza (inches): "))

    # Calculates price of the pizza
    subtotal = (
        constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST + diameter
    )
    tax = subtotal * constants.HST
    total = subtotal + tax

    # Displays the final total of the pizza back to the user
    print("")
    print("The total for your pizza is: ${:,.2f}".format(total))


# Outputs the function
if __name__ == "__main__":
    main()
