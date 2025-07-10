import random

last_pick = False
min_value = 0
max_value = 100
n= 0
com_number1 = False
com_number2 = False


scale = int(input("Enter how many times to run the experiment: "))






for x in range(0,scale):
    com_number2 = random.randint(0,100)
    while True:
        n = n + 1
        com_number1 = random.randint(min_value,max_value)
        
        if com_number1 == com_number2:
            min_value = 0
            max_value = 100
            break

        else:
            if com_number2 < com_number1:
                max_value = com_number1 -1 
            elif com_number2 > com_number1:
                min_value = com_number1 + 1


    

result = n / scale 

print(f"It took an average of {result} attempts to guess the number.") 
