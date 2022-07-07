#functions go here
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
def choice_checker(question, valid_list, error) :
#Main routine goes here

# Lists of valid response
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

#ask user if they have played before
#if yes, show instructions

#ask user for # rounds then loop
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
    choose_instruction = "Please choose from rock (r), paper (p), scissors (s) or xxx to quit"
    choose_error = "Please choose from rock, paper, scissors (or xxx to quit)"

    choose = choice_checker(choose_instruction, rps_list, choose_error) 

    if choose == "xxx":
        break

    rounds_played += 1
print("Thank you for playing") 

#ask user if they want to see their game history
#if yes, show instructions
