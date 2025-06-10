# Functions go here
def make_statement(statement, decoration):
    """Creates headings (3 lines), subheadings (2 lines) and emphasised text / mini-headings
    (1 line). Only use emoji for single line statements."""

    information = f"{decoration * 3} {statement} {decoration * 3}"

    print(information)



def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
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
    make_statement("Instructions", "🍟")

    print(''''
          
For each ticket holder enter ...
    - Their name 
    - Their age
    - The payment method (cash / credit)
    
The program will record the ticket sale and calculate the
ticket cost 9and the profit).

Once you have either sold all of the tickets or entered the
exit code ('xxx'), the program will display the ticket 
sales information and write the data to a text file. 

It will also choose one lucky ticket holder who wins the 
draw (their ticket is free). 

      ''')


# Main routine goes here

make_statement("Mini-Movie Fundraiser Program", "🍟")

print()
want_instructions = string_check("Do you want to see the instruction? ")

if want_instructions == "yes":
    instructions()

print()
print("program continues...")