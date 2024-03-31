import time

def main():
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

        print(f"\n-----------------------------")

        for command, meaning in commands.items():
            print(f"\n{command}: {meaning}")
        print(f"\nwrite 'stop' while making a new tasks to cancel ")
            
        print(f"\n-----------------------------\n")

    commands_print()

    def current_date():
        date_now = time.localtime()
        year = (date_now.tm_year)
        month = (date_now.tm_mon)
        day = (date_now.tm_mday)

        print(f"{year}-{month}-{day}")

    while isactive:


        x = input()

        def get_task():
            """the user gets to input a tasks and a deadline whick is stored in the tasks dict"""
            task = input(f"\nWhat task would you like to write down? ").title()
            if task == "Stop":
                if tasks == True:
                    del tasks[-1]
                    remaining_tasks()
                else:
                    remaining_tasks()
            task_date = input(f"\nWhat is the deadline of the task? ").lower()
            if task_date == "stop":
                if tasks == True:
                    del tasks[-1]
                    remaining_tasks()
                else:
                    remaining_tasks()
            weekdays = {"mon" : "monday",
                        "tue" : "tuesday",
                        "wed" : "wednesday",
                        "thu" : "thursday",
                        "fri" : "friday",
                        "sat" : "saturday",
                        "sun" : "sunday"}
        
            if task_date in weekdays:
                task_date = weekdays[task_date]
                tasks[task] = task_date
            else:
                tasks[task] = task_date


        def remaining_tasks():
            """ shows the remaining tasks"""

            if bool(tasks) == True:

                task_number = 1

                print(f"\n-----------------------------\n")

                for task, task_date in tasks.items():
                    print(f"{task_number}. {task} is due to {task_date}") #add how many days are left
                    task_number += 1

                print(f"\n-----------------------------\n") #the lines should seperate tasks based on due days
            
            else:
                print(f"\n-----------------------------\n")
                print(f"No tasks due. ")
                print(f"\n-----------------------------\n")
            

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

main()

#date isn't properly formated ####-##-##
#writing the same tasks but on different days doesn't work