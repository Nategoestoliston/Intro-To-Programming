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
        
#Main routine goes here
show_instructions = yes_no("Have you played this game before? ")

print("You choose {}" .format(show_instructions))