tasks = {}
isactive = True
commands = {
   
"new" : "creates new task ",
"quit" : "exits the program ",
"tasks" : "shows all undone tasks ",
"done" : "delete a task"  

}

print(f"\n-----------------------------")

for command, meaning in commands.items():
    print(f"\n{command}: {meaning}")
    
print(f"\n-----------------------------\n")

while isactive:


    x = input()

    def get_task():
        task = input(f"\nWhat task would you like to write down? ").title()
        task_date = input(f"\nWhat is the deadline of the task? ")
        tasks[task] = task_date

    def remaining_tasks():

        if bool(tasks) == True:

            task_number = 1

            print(f"\n-----------------------------\n")

            for task, task_date in tasks.items():
                print(f"{task_number}. {task} is due to {task_date}") #add how many days are left
                task_number += 1

            print(f"\n--------------------\n") #the lines should seperate tasks based on due days
        
        else:
            print(f"\n-----------------------------\n")
            print(f"No tasks due. ")
            print(f"\n-----------------------------\n")
        

    if x == "new":
        get_task()


    elif x == "q" or x == "exit" or x == "quit":
        isactive = False


    elif x == "tasks":
        remaining_tasks()
    

    elif x == "done":
        y = input("What task did you complete? ").title()

        while y not in tasks:
            y = input((f"\nThis task doesn't exist. What task did you complete? ")).title()

        if y in tasks:
            del tasks[y]
            remaining_tasks()