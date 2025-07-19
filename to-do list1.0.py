
STRIKETHROUGH = "\033[9m"
RESET= "\033[0m"

def create():
    try: 
        pass
    except FileNotFoundError:
        with open("to-dolist.txt","w") as f:
            pass

def add():
    task_add = input("Add a task: ")
    with open("to-dolist.txt","a") as f:
        f.write(task_add + "\n")

def read():
    x= 0
    with open("to-dolist.txt") as fs:
        for line in fs:
            x = x + 1
            print(f"{RESET}{x})" ,line.strip())
            
    #f = open("to-dolist.txt")
    #with open("to-dolist.txt","r") as f:
     #   for x in range(0,len(f.readlines())):
      #      with open("to-dolist.txt", "r") as fs:
       #         line = fs.readlines(x)
        #        print("Read line:", line)



    #fs = open("to-dolist.txt")
    #print(fs.read())

    #with open("to-dolist.txt",) as f:

        #lines = len(f.readlines())
        #print('Total Number of lines:', lines)
        #print(f.readlines())
        #print(f.read())
        #for x in range(0,len(f.readlines())):
         #   print(f.readlines())

def delete(x):
    try:
        while True:
            if not x > line_count:    
                with open("to-dolist.txt","r") as fr:
                    lines = fr.readlines()
                    ptr = 1 

                    with open("to-dolist.txt","w") as fw: 
                        for line in lines:
                            if ptr != x:
                                fw.write(line)
                            ptr += 1 
                            
            else:
                x = input("Please write an accurate line to delete: ")
            
    except:
        print("Ops!!")

def finished(x):
    try:
        while True:
            if not x > line_count:           
                with open("to-dolist.txt","r") as fr:
                    lines = fr.readlines()
                    ptr = 1 

                    with open("to-dolist.txt","w") as fw: 
                        for line in lines:
                            if ptr != x:
                                fw.write(line)
                            else:
                                fw.write(f"{STRIKETHROUGH}{line}{RESET}")
                            ptr += 1 
            else:
                x = input("Please write an accurate line to delete: ")
    except:
        print("Oops!!")


with open("to-dolist.txt","x") as fw:
    with open("to-dolist.txt","r") as f:
        lines = f.readlines()
        line_count = 0
        for line in lines:
            line_count += 1 
        

while True:
    task = input("Type add to add a task, read to view your to-do list, or q to quit: ")
    if task == "add":
        add()
    elif task == "read":
        read()
        task_1 = input("Select what you want to do: d to delete, m to mark a task as done, or q to quit:")
        if task_1 == "d":
            delete(int(input("Write the number you want to delete: ")))
        elif task_1 == "m": 
            finished(int(input("Write the number of the task you have finished: ")))
        elif task_1 == "q":
            quit
        
    elif task == "q":
        break

