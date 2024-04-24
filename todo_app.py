import datetime as dt


tasks = {}
isactive = True
commands = {

"new" : "creates new task ",
"quit" : "exits the program ",
"tasks" : "prints all undone tasks ",
"done" : "delete a task",
"date" : "prints current date",
"help" : "prints all commands",


}

def commands_print():
    """prints all commands"""

    print(f"\n-----------------------------------------------")

    for command, meaning in commands.items():
        print(f"\n{command}: {meaning}")
    print(f"\nwrite 'cancel' while making a new tasks to cancel ")
        
    print(f"\n-----------------------------------------------\n")

commands_print()

def current_date():

    today = dt.date.today()
    year = (today.year)
    month = (today.month)
    day = (today.day)

    date_now = f"{year}-{month:02d}-{day:02d}" #:02d makes integers from 1 to 9 have leading zeroes 

def days_left(future):

    future = future.split("-")
    year = int(future[0])
    month = int(future[1])
    day = int(future[2])
    future = dt.date(year, month, day)
    today = dt.date.today()
    diff = (future - today).days
    return diff

    

while isactive:

    x = input()

    def get_task():
        """the user gets to input a tasks and a deadline which is stored in the tasks dict"""

        while 1:

            task = input(f"\nWhat task would you like to write down? ").title()

            if task == "Cancel":
                break

            future = input(f"\nWhat is the deadline of the task? Format date as YYYY-MM-DD: ")


            if future == "cancel":
                break

            else:
                tasks[task] = future
                break

        remaining_tasks()



    def remaining_tasks():
        """ shows the remaining tasks"""

        if tasks:

            task_number = 1

            print(f"\n-----------------------------------------------\n")

            for task, future in tasks.items():

                difference = days_left(future)
                print(f"{task_number}. {task} is due to {future} | {difference} days left.")
                task_number += 1

            print(f"\n-----------------------------------------------\n") 
        
        else:
            print(f"\n-----------------------------------------------\n")
            print(f"No tasks due. ")
            print(f"\n-----------------------------------------------\n")
        

    if x == "new":
        get_task()


    elif x == "q" or x == "exit" or x == "quit":
        isactive = False

    elif x == "date":
        current_date()

    elif x == "help":
        commands_print()

    elif x == "tasks":
        remaining_tasks()
    

    elif x == "done":
        y = input(f"\nWhat task did you complete? ").title()

        while y not in tasks:
            y = input((f"\nThis task doesn't exist. What task did you complete? ")).title()

        if y in tasks:
            del tasks[y]
            print(f"\nMarked {y} as done ")
            remaining_tasks()



"""currently pretty shitty, will come back to it"""
#
#
#
# writing the same tasks but on different days doesn't work
# should be able to enter the tasks number to mark it as done
# --- lines should seperate tasks based on due days