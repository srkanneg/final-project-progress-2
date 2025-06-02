import classes

while True:
    entry = input("\nWhat would you like to do? (Options: add task, remove task, view tasks, view_completed_tasks, exit): ")
    
    if entry == "add task":
        name = input("\nWhat will be the name of the task?: ")
        description = input("\nWhat will be the description?: ")
        
        try:
            due_date = int(input("\nWhat will be the due date? (YYYYMMDD): "))
        except:
            print("\nMust use correct format!")
            continue
        
        category = input("\nWhat category should the task be placed in?: ")
        
        try:
            time = int(input("\nWhat time of day should the task be completed? (24-hour, HHMM): "))
        except:
            print("\nMust use correct format!")
            continue
        
        completed = input("\nIs the task already completed? (True or False): ")
        
        if completed == "True":
            completed = True
        elif completed == "False":
            completed = False
        else:
            print("Must enter a value exactly as shown!")
            continue
        
        location = input("\nWhere will the task be completed?: ")
        obj = classes.Task(name, description, due_date, category, time, completed, location)
        print("\nTask created successfully! The details of this task are: \n\n" + str(obj) + "\n")
        classes.TodoList(obj).add_task()
        continue
    
    elif entry == "remove task":
        print("These are the current tasks: ")
        for i in range(len(classes.tasks)): # Supposed to be a function to print the name of each task in the to-do list given a list of Task objects
            print("\n" + classes.tasks[i].name)
        which = input("\nEnter the name of the task that you want to remove exactly as shown above or enter \"exit\" to return back to the main menu: ")
        if which == "exit":
            continue
        for x in range(len(classes.tasks)): # Supposed to be a function that takes a list of Task objects and removes the ones that the user wants to remove
            if which == classes.tasks[x].name:
                classes.tasks.remove(classes.tasks[x])
                break
        print("\nTask removed successfully! The to-do list is now:")
        if len(classes.tasks) == 0:
            print("Empty")
        for i in range(len(classes.tasks)):
            print("\n" + classes.tasks[i].name)
        continue
    
    elif entry == "view tasks":
        print("\nThe total list of to-do list tasks are: ")
        for i in range(1, len(classes.tasks)): # Supposed to be a function that takes a list of Task objects and sorts it by due date in ascending order
            temp = classes.tasks[i]
            j = i - 1
            while j >= 0 and temp.due_date < classes.tasks[j].due_date:
                classes.tasks[j + 1] = classes.tasks[j]
                j -= 1
            classes.tasks[j + 1] = temp
        for i in range(len(classes.tasks)): # Supposed to be a function to print the name of each task in the to-do list given a list of Task objects
            print(classes.tasks[i].name + "\n")
            
    elif entry == "view completed tasks":
        updated_tasks = []
        for i in range(1, len(classes.tasks)): # Supposed to be a function that takes a list of Task objects and sorts it by due date in ascending order
            temp = classes.tasks[i]
            j = i - 1
            while j >= 0 and temp.due_date < classes.tasks[j].due_date:
                classes.tasks[j + 1] = classes.tasks[j]
                j -= 1
            classes.tasks[j + 1] = temp
        for j in classes.tasks: # Supposed to be a function that takes a list of Task objects and filters out the ones that are not complete
            if classes.tasks[j].completed == False:
                updated_tasks.append(classes.tasks[j])
        for x in range(len(updated_tasks)): # Supposed to be a function to print the name of each task in the to-do list given a list of Task objects
            print(updated_tasks[x].name + "\n")

    elif entry == "exit":
        break
    
    else:
        print("Invalid command! Please enter one of the options shown above exactly as shown!")
        continue