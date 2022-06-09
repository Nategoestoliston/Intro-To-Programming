from urllib import response


error = "Please enter an whole number between 1 and 10"

valid = False
while not valid:
    response = int(input("How much would you like to play with? "))

    if 0 < response <= 10:
        print("You have asked to play with ${}".format(response))

    else:
        print(error)