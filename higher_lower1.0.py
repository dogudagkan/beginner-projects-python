import random

rnumber = random.randint(1,100)

def get_number():
    while True:
        try:
            return int(input("Please pick a number between 1 and 100: "))
        except ValueError:
            print("Please pick a number !!")


while True:
    Dnumber = get_number()

    if not 0 <= Dnumber <= 100:
        pass
    elif Dnumber < rnumber: 
        print("Higher")
    elif Dnumber > rnumber:
        print("lower")
    elif Dnumber == rnumber:
        print("Congrats !!!")

