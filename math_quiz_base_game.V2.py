import math
import random

def instructions () :
    """Prints instructions"""

    print("""
*** Instructions ****

Start by choosing an operation (+)
Then you will have to answer 3 questions about the chosen operation eg 1 + 4 or 10 + 5
The range of numbers is 1 - 10
Good luck!


    """)
def string_checker(question , valid_ans=("yes", "no")):

    error = f"please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            #check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

def int_check(question):
    while True:
        error = "sorry that answer is incorrect"

        to_check = input(question)

        try:
            response = int(to_check)

            if op_checker == "+":
                if response != random_interger + random_interger_2:
                    print(error)
                else:
                    return response
            if op_checker == "-":
                if response != random_interger - random_interger_2:
                    print(error)
                else:
                    return response
            if op_checker == "*":
                if response != random_interger * random_interger_2:
                    print(error)
                else:
                    return response
            if op_checker == "/":
                if response != random_interger / random_interger_2:
                    print(error)
                else:
                    return response

        except ValueError:
            print(error)

def int_check_2(question):
    while True:
        error = "sorry that answer is incorrect"

        to_check = input(question)

        try:
            response = int(to_check)

            if op_checker == "+":
                if response != random_interger_3 + random_interger_4:
                    print(error)
                else:
                    return response
            if op_checker == "-":
                if response != random_interger_3 - random_interger_4:
                    print(error)
                else:
                    return response
            if op_checker == "*":
                if response != random_interger_3 * random_interger_4:
                    print(error)
                else:
                    return response
            if op_checker == "/":
                if response != random_interger_3 / random_interger_4:
                    print(error)
                else:
                    return response

        except ValueError:
            print(error)

def int_check_3(question):
    while True:
        error = "sorry that answer is incorrect"

        to_check = input(question)

        try:
            response = int(to_check)

            if op_checker == "+":
                if response != random_interger_5 + random_interger_6:
                    print(error)
                else:
                    return response
            if op_checker == "-":
                if response != random_interger_5 - random_interger_6:
                    print(error)
                else:
                    return response
            if op_checker == "*":
                if response != random_interger_5 * random_interger_6:
                    print(error)
                else:
                    return response
            if op_checker == "/":
                if response != random_interger_5 / random_interger_6:
                    print(error)
                else:
                    return response

        except ValueError:
            print(error)
#game starts here
# instructions
want_instructions = string_checker("Do you want to see the instructions? ")

# return instructions
if want_instructions == "yes" :
    instructions()

#operation list
op_list = ["+","-","*","/", "xxx"]

# game heading
print("➕➖✖️➗ Basic facts quiz ️➗️✖️➖➕")
print()

# allow user to choose a operation
op_checker = string_checker("Choose an operation ", op_list)

# randomise first number
min_value = 1
max_value = 10
random_interger = random.randint(min_value, max_value)

#randomise second number
min_value_2 = 1
max_value_2 = 10
random_interger_2 = random.randint(min_value_2, max_value_2)

# randomise first number
min_value_3  = 1
max_value_3 = 10
random_interger_3 = random.randint(min_value_3, max_value_3)

#randomise second number
min_value_4 = 1
max_value_4 = 10
random_interger_4 = random.randint(min_value_4, max_value_4)

# randomise first number
min_value_5  = 1
max_value_5 = 10
random_interger_5 = random.randint(min_value_5, max_value_5)

#randomise second number
min_value_6 = 1
max_value_6 = 10
random_interger_6 = random.randint(min_value_6, max_value_6)

# create question 1
Q_A = int_check(f"{random_interger} {op_checker} {random_interger_2} = ")
print("first quesiton =", Q_A)

# create question 2
Q_A_2 = int_check_2(f"{random_interger_3} {op_checker} {random_interger_4} = ")
print("second quesiton =", Q_A_2)

# create question 3
Q_A_3 = int_check_3(f"{random_interger_5} {op_checker} {random_interger_6} = ")
print("thrid quesiton =", Q_A_3)

#display history
see_history = string_checker("\nDo you want to see your game history? ")

if see_history == "yes":
    print(f"Q_A = {Q_A}\t"
          f"Q_A_2 = {Q_A_2}\t"
          f"Q_A_3 = {Q_A_3}")
# output game stats