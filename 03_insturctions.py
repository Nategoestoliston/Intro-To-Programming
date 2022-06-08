#functions go here

# from urllib import response


def  yes_no(question):
    
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or  response == "y":
            response = "yes"
            print("Program continues")
            return response

        elif response == "no" or response == "n":
            response == "no"
            print("display instructions")
            return response

        else:   
            print("Please answer yes / no")


def instructions():
    print("***** How to play *****")
    print()
    print("The rules of the game go here")
    print()
    return ""


#Main routine goes here
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()
    
    
print("Program Continues")

# print("You choose {}" .format(played_before))