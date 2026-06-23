

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
    task = input("\nAdd task: ")
    tasks.append(task)
    return

def modify_tasks(tasks):
    print_tasks(tasks)
    modify_option = int(input("Which task would you like to modify?"))
    modify_change = input("What task would you like to call it now? ")
    old_version = tasks[modify_option-1]
    tasks[modify_option - 1] = modify_change
    print("The task has been succesfully been changed from", old_version, "to",modify_change)
    return

def delete_tasks(tasks):
    print_tasks(tasks)
    modify_option = int(input("Which task would you like to delete?"))
    old_version = tasks[modify_option - 1]
    tasks.pop(modify_option - 1)


    print("The task", old_version, "has been succesfully deleted.")
    return

def print_tasks(tasks):
    
    count = 0 
    for t in tasks:
        if count == 0:
            print("\nTasks: ")
        count += 1
        print(str(count)+".", t)
    
    return

def saving_to_file(tasks): 
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    tasks = []
    
    try: 
        with open("tasks.txt","r") as file: 
            for line in file:
                tasks.append(line.strip())
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
    
        


