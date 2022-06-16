import random

#main routine goes here
tokens = ["unicorn", "horse", "zebra", "donkey"]

#Testing loops to generate 20 tokens
for item in range ( 0, 20):
    chosen = random.choice(tokens)
    print(chosen, end='\t')