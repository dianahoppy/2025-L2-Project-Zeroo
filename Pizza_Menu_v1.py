import pandas
import numpy as np
from pandas import DataFrame

# lists to hold ticket details
pizza = ["Cheese", "Peperoni", "Meat Lovers", "Hawaiian", "Vegetarian"]
extras = ["Fries", "Pearly's Soda Pop"]
pizza_costs = [7.50, 7.50, 9.00, 9.00, 9.00]
extras_costs = [3.00, 4.50]

pizza_dict = {
    'Pizzas': pizza,
    'Pizza Price': pizza_costs

}

# Work out total paid and total profit...
total_paid = sum(pizza_costs)
#total_profit = pizza_dict['profit'].sum()

print(f"Total Paid: ${total_paid:.2f}")
#print(f"Total Profit: ${total_profit:.2f}")

# create dataframe / table from dictionary
pizza_frame: DataFrame = pandas.DataFrame(pizza_dict)

# Rearranging index
pizza_frame.index = np.arange(1, len(pizza_frame) + 1)

print(pizza_frame)
print()

