
import json

def options(tasks):
    print("\nWhat would you like to do?\n")
    print(" a. Add Task\n b. Modify Tasks\n c. Delete Tasks\n d. End Tasks List")
    option = input("")
    if option == 'a':
        add_tasks(tasks)
    elif option == 'b':
        modify_tasks(tasks)
    elif option == 'c': 
        delete_tasks(tasks)
    elif option == 'd':
        return 'stop'
    return 'continue'
        

def add_tasks(tasks):
    ask = input("\nAdd task: ")
    ##tasks.append(task)
    next_number = len(tasks) + 1
    
    tasks[next_number] = ask
    return

def modify_tasks(tasks):
    print_tasks(tasks)
    modify_option = str(input("Which task would you like to modify?"))
    modify_change = input("What task would you like to call it now? ")
    
    old_version = tasks[modify_option]
    
    tasks[modify_option] = modify_change
    print("The task has been succesfully been changed from", old_version, "to",modify_change)
    return

def delete_tasks(tasks):
    print_tasks(tasks)
    modify_option = str(input("Which task would you like to delete?"))
    old_version = tasks[modify_option]
    
    
    tasks.pop(modify_option)

    tasks ={index: task for index, task in enumerate(tasks.values(), start=1)}


    print("The task", old_version, "has been succesfully deleted.")
    return

def print_tasks(tasks):
    
    print("Task lists: ")
    for item in tasks:
        print(item, tasks[item])


    ##count = 0 
    ##for t in tasks:
      ##  if count == 0:
        ##    print("\nTasks: ")
        ##count += 1
        ##print(str(count)+".", t)
    
    return

def saving_to_file(tasks): 
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=1)
        


def load_tasks():
    tasks = dict()
    
    try: 
        with open("tasks.json","r") as file: 
            tasks = json.load(file)
    except FileNotFoundError:
        pass
    return tasks


tasks = load_tasks()

while True:
    control = options(tasks)
    
    if control == 'stop':
        print("You're final task list is as follows:")
        print_tasks(tasks)
        save_option = input("Would you like to save these into a file (Y/N)? ")
        if save_option == 'Y' or save_option == 'y':
            saving_to_file(tasks)

        break
    
    print_tasks(tasks)
    
        


