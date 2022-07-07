from distutils.log import error
from urllib import response


def choice_checker(question, valid_list, error) :
    error = "Please choose from rock / paper / scissors (or xxx to quit)"

    valid = False
    while not valid :

        response = input(question).lower()
        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response == "scissors":
            return response
        elif response == "xxx" :
            return response
        else:
            print(error)
rps_list = ["rock", "paper", "scissors", "xxx"]   

user_choice = ""
while user_choice != "xxx":
    user_choice = choice_checker ("Choose rock / paper / scissors (r/p/s) :", rps_list, "Please choose from rock / paper / scissors (or xxx to quit")
    print("you chose {}".format(user_choice))