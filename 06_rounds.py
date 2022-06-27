balance = 5

round_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    round_played += 1

    print("*** Round #{} ***".format(round_played))
    print(round_played)
    balance -= 1
    print("Balance: ", balance)
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or XXX to quit")