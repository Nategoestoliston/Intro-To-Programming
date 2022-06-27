balance = 5

round_played = 0

play_again = input("Press <Enter> to play...")
while play_again == "":
    round_played += 1
    print(round_played)
    balance -= 1
    print("Balance: ", balance)
    print()
    play_again = input("Press Enter to play again or XXX to quit")