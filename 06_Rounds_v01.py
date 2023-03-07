# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...")
while play_again == "":
    # increase # of rounds played
    rounds_played += 1


    # Print round number
    print("*** Round #{} ***".format(rounds_played))
