from typing import Dict, Union, List

import pandas
import numpy as np
from pandas import DataFrame


# Functions go here
def phone_check(number):
    """Checks users enter an integer 10 digits long"""

    error = f"Oops - please enter a number that has 10 numbers"

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(number))
            ph_number = len(str(response))

            if ph_number == 10:
                return ph_number
            else:
                print(error)

        except ValueError:
            print(error)


def int_check(question, low, high):
    """Checks users enter an integer between two values"""

    error = f"Oops - please enter an integer between {low} and {high}"

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def make_statement(statement, decoration):
    """Creates headings (3 lines), subheadings (2 lines) and emphasised text / mini-headings
    (1 line). Only use emoji for single line statements."""

    information = f"{decoration * 1} {statement} {decoration * 1}"

    print(information)


def string_check(question, valid_answers, num_letters=1):
    """Checks that users enter the full word
        or the 'n' letter/s of a word from a list of valid responses"""

    while True:
        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def instructions():
    make_statement("Instructions", "🍕")

    print('''

Welcome to Pearly's Pizzeria.

For each customer enter ...
    - Their name 
    - Their number
    - Whether they are picking up or getting a delivery
    - If delivering, then their address
    - Their order, and if they'd like any sides

The program will record the pizza order and calculate the
pizza cost and the profit.

Once you have entered the exit code ('xxx'), the program will display the pizza
order information and write the data to a text file. 

      ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry this can't be blank. Please try again. \n")


# Variables


yes_no = ["yes", "no"]
pickup_del = ["pickup", "delivery"]

# lists to hold order details
user_pizza_order = []
user_pizza_order_prices = []
user_sides_order = []
user_sides_order_prices = []

pizza = ["Cheese", "Pepperoni", "Meat Lovers", "Hawaiian", "Vegetarian"]
sides = ["Fries", "Pearly's Soda Pop", "No sides"]
pizza_costs = [7.50, 7.50, 9.00, 9.00, 9.00]
sides_costs = [4.50, 3.00, 0.00]

pizza_dict = {
    'Pizzas': pizza,
    'Pizza Price': pizza_costs
}

sides_dict = {
    'Sides': sides,
    'Sides Price': sides_costs

}

order_dict = {
    'Pizzas': user_pizza_order,
    'Pizza Price': user_pizza_order_prices,
    'Sides': user_sides_order,
    'Sides Price': user_sides_order_prices

}

# main program heading
make_statement("Pearly's Pizzeria", "👨‍🍳")

make_statement("Welcome to Pearly's Pizzeria, where hot and fresh pizza deals are our guarantee!", "🍕")

print()
want_instructions = string_check("Do you want to see the instructions? ", yes_no)

if want_instructions == "yes":
    instructions()

print()

name = not_blank("Please enter your name: ")
print()

number = phone_check("Please enter your phone number - 10 digits: ")
print()

delivery_type = string_check(f"Greetings {name}. Is the order pickup or delivery? ", pickup_del)
print()

print(f"You chose {delivery_type}")

if delivery_type == "delivery":
    address = not_blank("Please enter your address: ")
    delivery_surcharge = 20

print()

# create dataframe / table from dictionary
pizza_frame: DataFrame = pandas.DataFrame(pizza_dict)
sides_frame: DataFrame = pandas.DataFrame(sides_dict)

# Rearranging index
pizza_frame.index = np.arange(1, len(pizza_frame) + 1)
sides_frame.index = np.arange(1, len(sides_frame) + 1)

# Ask how many pizzas

num_of_pizzas = int_check("How many pizzas for this order? ", 1, 5)

for xyz in range(num_of_pizzas):
    print(pizza_frame)

    user_pizza_selection = int_check("Enter the number of your pizza: ", 1, 5)
    print()

    print(f"You chose {pizza[user_pizza_selection - 1]} ${pizza_costs[user_pizza_selection - 1]}")
    user_pizza_order.append(pizza[user_pizza_selection - 1])
    user_pizza_order_prices.append(pizza_costs[user_pizza_selection - 1])

    print(sides_frame)

    user_sides_selection = int_check("Enter the number of your sides: ", 1, 3)

    print(f"You chose {sides[user_sides_selection - 1]} ${sides_costs[user_sides_selection - 1]}")
    user_sides_order.append(sides[user_sides_selection - 1])
    user_sides_order_prices.append(sides_costs[user_sides_selection - 1])


order_frame: DataFrame = pandas.DataFrame(order_dict)

print(order_frame)

# testing total pizza costs
total_pizza_costs = sum(user_pizza_order_prices)

# testing total pizza costs
total_sides_costs = sum(user_sides_order_prices)
print()


print(f"Total pizza costs: ${total_pizza_costs}")
print(f"Total sides costs: ${total_sides_costs}")
if delivery_type == "":
    print(f"Delivery costs: ${delivery_surcharge}")
print(f"Total pizza costs: ${total_pizza_costs}")
print(f"Total costs: ${total_pizza_costs + total_sides_costs}")
print()

# total_profit = pizza_dict['profit'].sum()

# Work out total paid and total profit...
#total_paid = sum(pizza_costs)
#total_paid = sum(sides_costs)

# print(f"Total Paid: ${total_paid:.2f}")

make_statement("Thank you for supporting Pearly's Pizzeria!", "🍕")
print()

