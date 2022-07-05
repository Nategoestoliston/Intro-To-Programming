def check_rounds():

    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter>  \ or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)
                
                if response < 1:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue
        return response

rounds_played = 0
choose_instruction = "Please choose rock (r), paper (p), scissors (s)"

rounds = check_rounds()

end_game = "no"
while end_game =="no":
    print()
    if rounds == "":
        heading = "Continuons mode : Round {}".format(rounds_played + 1)

    else :
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
    print(heading)
    choose = input("{} or 'xxx' to end: ".format(choose_instruction))

    if choose == "xxx":
        break

    rounds_played += 1
print("Thank you for playing") 