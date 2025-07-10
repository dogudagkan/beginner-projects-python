import random

last_pick = False
min_number = 0
max_number = 100

n = 0


def user_number():
    while True:
        try: 
            return int(input("Pick a number between 1 and 100: "))
        except ValueError:
            print("Please pick a number !!")


        

u_pick = user_number()

while True:
    last_pick = random.randint(min_number,max_number)
    
    if u_pick == last_pick:
        print(f"The number you picked is {u_pick}!!!")
        print(f"It took me {n} tries to guess your number.")
        break
    elif not u_pick == last_pick:
        n = n + 1
        tries = input(f"Is your number {last_pick}? (Enter 'l' for lower, 'h' for higher): ") 

        if tries == "l": #pick a smaller number
            max_number = last_pick - 1

        elif tries == "h":
            min_number = last_pick + 1

