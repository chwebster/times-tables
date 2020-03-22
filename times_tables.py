"""
Times Tables Game

A game for practising times tables.

Ten sums are generated and the player is prompted to answer.

Each answer is marked correct or incorrect.
If incorrect, the correct answer is given.

At the end of the test a score is given, along with suitable praise.

If full marks are achieved, the time taken is also given as an incentive
to practise more and get faster.
"""

# import the module random to allow us to generate random numbers:
import random

# import the function time from the module time to allow us to time a process:
from time import time

# Define a function to report the time taken:
def report_time(mins, secs):
    if mins == 0:
        return "You took {} seconds.".format(secs)
    elif mins == 1 and secs == 1:
        return "You took {} minute and {} second.".format(mins, secs)
    elif mins == 1 and secs != 1:
        return "You took {} minute and {} seconds.".format(mins, secs)
    elif secs == 1:
        return "You took {} minutes and {} second.".format(mins, secs)
    else:
        return "You took {} minutes and {} seconds.".format(mins, secs)

# Define a function to give suitable praise, depending on score:
def praise(score):
    if score < 1:
        return "Oh dear!"
    elif score <= 4:
        return "Not bad!"
    elif score <= 7:
        return "Good effort!"
    elif score <= 9:
        return "Good job!"
    else:
        praise_options = ["Awesome!", "Brilliant!", "Fantastic!", "Amazing!",
                          "Fabulous!", "Top Marks!", "A perfect score!", "Superb!"]
        return random.choice(praise_options)

# Run the program only if it is not being imported as a module or from the help:
if __name__ == '__main__':
    print("\nHello and welcome to the Times Tables Game!")
    print("You will be given 10 questions. Try to get as many correct as possible.\n")

    # Initialise the count of correct answers:
    correct_count = 0

    # Start the timer:
    start = time()

    # Set 10 questions:
    for i in range(10):
        # Generate two random numbers between 2 and 12:
        a = random.randint(2, 12)
        b = random.randint(2, 12)

        # Get user input for the answer to a * b,
        # if an invalid answer is entered, ask the question again:

        # Keep going round this loop until an integer is entered:
        while True:
            # Test whether an error occurs, e.g. if return is pressed before a
            # number is entered:
            try:
                # Get user input and convert it to a number:
                c = eval(input("{} x {} = ".format(a, b)))
                # Test whether the input is an integer:
                if type(c) != int:
                    # If input is non-integer, e.g. text, continue going
                    # round the while loop:
                    continue
                    # If no error has occurred and input is integer, exit while loop:
                break
                # The code after this command only executes if there is an error:
            except:
                # If there's an error, continue going round the while loop:
                continue

        # Check whether the answer entered is correct:
        if c == a * b:
            print("Correct\n")
            correct_count += 1
        # If not, provide the correct answer:
        else:
            print("No, {} x {} = {}\n".format(a, b, a * b))

    # The 10 questions are finished. Stop the timer:
    end = time()
    time_taken = int(end - start)
    minutes = time_taken // 60
    seconds = time_taken % 60

    # Now provide the results with praise and encouragement:
    print(praise(correct_count) + " You scored {} out of 10.".format(correct_count))
    if correct_count < 10:
        print("Keep trying. Practise + effort + time = success!")
    else:
        print(report_time(minutes, seconds))
        print("Have another go! See if you can be even faster!")

    # Print a blank line to separate the final report from the command prompt:
    print()
