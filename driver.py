import classes
import functions

while True:
    entry = input("\nWhat would you like to do? (Options: add task, remove task, view tasks, view completed tasks, view incomplete tasks, view category, get status, export to file, exit): ")
    
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
        to_do_object = classes.TodoList(obj)
        add_list = to_do_object.add_task()
        continue
    
    elif entry == "remove task":
        print("\nThe to-do list currently consists of: \n")
        functions.view_tasks()
        which = input("\nEnter the name of the task that you want to remove exactly as shown above or enter \"exit\" to return back to the main menu: ")
        if which == "exit":
            continue
        classes.TodoList(which).remove_task()
        print("\nThe to-do list now consists of: \n")
        functions.view_tasks()
        continue
    
    elif entry == "view tasks":
        print("\nThe to-do list currently consists of: \n")
        functions.view_tasks()
        continue
            
    elif entry == "view completed tasks":
        print("\nThe completed tasks are: ")
        functions.sort_due_date()
        classes.TodoList().view_completed_tasks()
        continue
    
    elif entry == "view incomplete tasks":
        print("\nThe incomplete tasks are: ")
        functions.sort_due_date()
        classes.TodoList().view_incomplete_tasks()
        continue
        
    elif entry == "view category":
        print("\nThe current categories are: ")
        functions.view_categories()
        which = input("\nEnter the name of the category that you want to view the tasks for. Enter exactly as shown or enter \"exit\" to return back to the main menu: ")
        if which == "exit":
            continue
        print("\nThe tasks in this category are: ")
        classes.TodoList(which).view_category()
        continue
    
    elif entry == "get status":
        print("\nThe to-do list currently consists of: \n")
        functions.view_tasks()
        which = input("Enter the name of the task exactly as shown above to get the status of it, or type \"exit\" to return back to the main menu: ")
        if which == "exit":
            continue
        classes.TodoList(which).get_status()
        continue
        
    elif entry == "export to file":
        with open("exported_to_do_list.txt", "w") as file:
            for i in range(len(classes.tasks)):
                file.write("\n{}".format(str(classes.tasks[i])))
        print("\nMust type \"exit\" for export to take place.")
        continue

    elif entry == "exit":
        break
    
    else:
        print("Invalid command! Please enter one of the options shown above exactly as shown!")
        continue