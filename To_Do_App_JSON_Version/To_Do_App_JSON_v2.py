
## Each task will in itself be a dictionary 

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

def add_tasks(tasks): ## A Method To Add Tasks
    ask = input("\nAdd task: ")
    ##tasks.append(task)
    new_task = dict() ## Create a New Dictionary 
    Task_Number = len(tasks) + 1 ## Get the Length + 1 
    new_task[str(Task_Number)] = ask ## Insert the Ask Heere
    new_task["Status"] = "Not Done" ## Add a Status Bar in the Mean Time 
    tasks.append(new_task) ## adding the task into the array
    return

def modify_tasks(tasks): ## A Method to Modify the State of Tasks 
    print_tasks(tasks)
    modify_option = int(input("Which task would you like to modify?"))
    print("How would you like to change the task?")
    print(" a. Change name\n b. Change status?")
    modify_how = str(input(""))
    
    
    if modify_how == 'a':
        change_name(tasks,modify_option)
    elif modify_how == 'b':
        change_status(tasks, modify_option)
    
    return

def change_name(tasks,modify_option):
    modify_change = str(input("What task would you like to call it now? "))
    old_version = tasks[(modify_option -1)][str(modify_option)] 
    tasks[(modify_option - 1)][str(modify_option)]= modify_change
    print("The task has been succesfully been changed from", old_version, "to",modify_change)
    return
    
def change_status(tasks,modify_option):
    print("What status would you like it to be on now?")
    print(" a. Done\n b. Not Done")
    status_change = str(input(""))
    if status_change == "a":
        tasks[modify_option - 1]["Status"] ="Done"
    elif status_change == "b":
        tasks[modify_option - 1]["Status"] ="Not Done"
    return
    

def delete_tasks(tasks):
    print_tasks(tasks)
    modify_option = int(input("Which task would you like to delete?"))
    old_version = tasks[(modify_option - 1)][str(modify_option)] ## Gets me the name 
    
    tasks.pop((modify_option - 1)) ## Removes this value

    renumber_dict(tasks)

    print("The task", old_version, "has been succesfully deleted.")
    return

def renumber_dict(tasks):
    # Enumerate gives us sequential index loops starting at 1
    for new_num, item in enumerate(tasks, start=1):
        # 'Status' is preserved, we find the other dynamic key (the old number string)
        old_num = next(key for key in item.keys() if key != "Status")
        
        # If the number changed, swap the key name out inside the dictionary
        if old_num != str(new_num):
            item[str(new_num)] = item.pop(old_num)
    return


def print_tasks(tasks):
    
    
    
    print("Task lists: ")
    
    for item in tasks:
        task_num = str(next(key for key in item.keys() if key!="Status"))
        print(task_num+ ". " + item[task_num]+" | Status: "+item["Status"])
        




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
    ## I Want Tasks to be an Array of Dictionaries 
    
    tasks = []
    
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
    
        


