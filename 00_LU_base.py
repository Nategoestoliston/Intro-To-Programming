import random
#functions go here
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
    print("Choose a stating amount (minimum $1 , maximum $10). Then press <enter> to play. You will get either a horse, a zebra, a donkey or unicorn.")
    print("It costs $1 per round. Depending on your prize you might win some money back. Here's the pay out amounts")
    print("Unicorn: $5.00 (balance increases by $4)")
    print("Horse: $0.50 (balance increases by $0.50)")
    print("Zebra: $0.50 (balance increases by $0.50)")
    print("Donkey: $0 (balance decreases by $1)")
    return ""

def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            response = int(input(question))
            
            if low < response <= high:
               return response
            
            else:
                print(error)
        
        except ValueError:
            print(error) 

def statement_generator(statement, decoration) :

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

#Main routine goes here
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
        instructions()
        print("Program Continues")
        
#ask user how much they will play with
how_much = num_check("How much would you like to play with ? ", 0, 10,)
print("You will be spending ${}".format(how_much))

balance = how_much

round_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    round_played += 1

    print()
    print("*** Round #{} ***".format(round_played))
    
    chosen_num = random.randint(1, 100)
    # print(chosen, end='\t')

    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <=36:
        chosen = "donkey"
        balance -= 1
    else :
        if chosen_num % 2 == 0:
            chosen = "horse"
        else :
            chosen = "zebra"
        balance -=0.5
    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or XXX to quit") 