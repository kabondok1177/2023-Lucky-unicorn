# Functions go here...
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

        # Main routine go here


# Main Routine goes here...
played_before = yes_no("Have you played the "
                       "game before? ")
if played_before == "no":
    instructions()

    print()
# Ask user how much they want to play with
how_much = num_check("How much would you"
                     " like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))
