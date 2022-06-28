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
    print()
    print("The rules of the game go here")
    print()
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
#Main routine goes here
played_before = yes_no("Have you played this game before? ")
if played_before == "no":
        instructions()
        print("Program Continues")
        
#ask user how much they will play with
how_much = num_check("How much would you like to play with ? ", 0, 10,)
print("You will be spending ${}".format(how_much))
balance = 5

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