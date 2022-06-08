show_instructions = ""
while show_instructions.lower() !="xxx":

    #ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    #If they say yes, output 'program continues'
    if show_instructions == "yes":
        print("Program continues")

    if show_instructions == "y":
        print("Program continues")

    elif show_instructions == "no":
        print("display instructions")

    elif show_instructions == "n":
        print("display instructions")

    #If they say no, output 'display instructions'
    else:
        print("Please answer yes / no")

    print("You choose {}" .format(show_instructions))