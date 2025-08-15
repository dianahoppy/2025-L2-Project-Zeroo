import pandas
import numpy as np
from pandas import DataFrame


# Functions go here
def int_check(question,low,high):
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


def string_check(question, valid_answers,num_letters=1):
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
    - Whether they are picking up or delivering
    - If delivering, then their address
    - The payment method (cash / credit)

The program will record the pizza order and calculate the
ticket cost and the profit).

Once you have entered the exit code ('xxx'), the program will display the pizza
order information and write the data to a text file. 

      ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry this can't be blank. Please try again. S\n")

# Variables


yes_no = ["yes", "no"]
pickup_del = ["pickup", "delivery"]

# lists to hold ticket details
pizza = ["Cheese", "Peperoni", "Meat Lovers", "Hawaiian", "Vegetarian"]
extras = ["Fries", "Pearly's Soda Pop"]
pizza_costs = [7.50, 7.50, 9.00, 9.00, 9.00]
extras_costs = [3.00, 4.50]

pizza_dict = {
    'Pizzas': pizza,
    'Pizza Price': pizza_costs

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

Number = not_blank("Please enter your phone number: ")

delivery_type = string_check(f"Greetings {name}. Is the order pickup or delivery? ", pickup_del)


# create dataframe / table from dictionary
pizza_frame: DataFrame = pandas.DataFrame(pizza_dict)

# Rearranging index
pizza_frame.index = np.arange(1, len(pizza_frame) + 1)

print(pizza_frame)
print()

user_pizza_selection = int_check("Enter the number of your pizza: ", 1, 5)

print(f"You chose {pizza[user_pizza_selection - 1]}")



#total_profit = pizza_dict['profit'].sum()

# Work out total paid and total profit...
total_paid = sum(pizza_costs)

print(f"Total Paid: ${total_paid:.2f}")
#print(f"Total Profit: ${total_profit:.2f}")