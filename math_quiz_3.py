import random


# check users entered yes (y) or no (n)
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option: {valid_ans}"

    while True:
        response = input(question).lower()
        for ans in valid_ans:
            if response == ans or response == ans[0]:
                return ans
        print(error, "\n")


# Instructions for the game if user enters yes
def instructions():
    """Prints instructions"""

    print('''
*** Instructions ****

Start by choosing an operation (+)
Then you will have to answer 3 questions about the chosen operation eg 1 + 4 or 10 + 5
The range of numbers is 1 - 10
Good luck!
''')

# The number of questions the user wants
def questions_amount():
    """Ask the user how many questions they want or enter infinite mode."""
    while True:
        response = input("How many questions would you like? Press <Enter> for infinite mode: ")
        if response == "":
            return None
        try:
            num = int(response)
            if num > 0:
                return num
            else:
                print("Please enter a number more than 0.")
                print()
        except ValueError:
            print("Please enter a valid number.")
            print()


# Main routine
print()
print("     ➕ basic facts quiz ➕")
print()

# ask the user if they want to see the instructions and display
# them if requested
want_instructions = string_checker(" Do you want to see the instructions? ")

# checks user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# initial integer for score and question counter
quiz_questions = questions_amount()
score = 0
questions_count = 0
history = []

early_exit = False  # Track if user exits early

# loop until the user has answered all questions, and infinite mode
while True:
    if quiz_questions is not None and questions_count >= quiz_questions:
        break

    # Randomly generated integers between 1-20 for the questions
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)
    correct = first_number + second_number

    # asks the player the question with the random numbers
    while True:
        answer_input = input(f"Question {questions_count + 1}: What is the answer to {first_number} + {second_number}?: ")

        if answer_input.lower() == "xxx":
            print("\n why did you leave?, i'll see you next time i guess")
            early_exit = True
            break

        try:
            answer = int(answer_input)
            break
        except ValueError:
            print("Please enter a valid number ")
            print()

    if early_exit:
        break

    # checks if users answer is right and adds to the score if they are
    # also tells them what the answer is if they are wrong
    if answer == correct:
        print()
        print("correct\n")
        score += 1
        result = "correct"
    else:
        print()
        print("Incorrect")
        print(f"The answer was {correct}.")
        print()
        result = f"Incorrect (Correct answer: {correct})"

    # Add to history
    history.append(f"Q{questions_count + 1}: {first_number} + {second_number} = {answer} → {result}")
    questions_count += 1

# Final results
if not early_exit:
    print(f"you finished the quiz")
    print()
    print("Thanks for playing")


# Ask if user wants to view their history
if questions_count > 0:
    see_history = string_checker("\nWould you like to see your answer history?: ")
    if see_history == "yes":
        print("\nHistory:")
        print("-" * 30)
        for item in history:
            print(item)

