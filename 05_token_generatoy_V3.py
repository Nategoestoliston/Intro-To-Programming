import random

#main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
#Testing loops to generate 20 tokens
for item in range ( 0, 500):
    chosen_num = random.randint(1,100)
    # print(chosen, end='\t')

    if 1<= chosen_num == "unicorn":
        balance += 4
    elif chosen_num == "donkey":
        balance -= 1
    else :
        balance -=0.5

print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}". format(balance))