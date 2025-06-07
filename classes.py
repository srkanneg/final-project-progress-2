# Jack is the author of this file

tasks = []

class Task:
    def __init__(self, name: str, description: str, due_date: int, category: str, time: int, completed: bool, location: str) -> None:
        self.name = name
        self.description = description
        self.due_date = due_date
        self.category = category
        self.time = time
        self.completed = completed
        self.location = location
        # initializes a Task object
    
    def __str__(self) -> str: # returns a string representation of the Task object, listing every attribute
        return "The name of the task is: \"{}\"\nThe description is: \"{}\"\nThe due-date is: {}\nThe category of task is: \"{}\"\nThe time of day it is due is: {}\nIs the task completed?: {}\nThe location of the task is: \"{}\"".format(self.name, self.description, self.due_date, self.category, self.time, self.completed, self.location)

class TodoList:
    def __init__(self, task_name: str = None):
        self.task_name = task_name
    
    def get_status(self) -> None: # checks if a task object is completed, checks if completed == True and prints a statement for the status
        ins_tasks = []
        for i in range(len(tasks)):
            if self.task_name == tasks[i].name and tasks[i].completed:
                ins_tasks.append(tasks[i])
        if len(ins_tasks) == 1:
            print("\nStatus: Completed")
        elif len(ins_tasks) == 0:
            print("\nStatus: In Progress")
        else:
            print("\nSomething went wrong, please reach out to the developers.")
    
    def mark_as_complete(self) -> None: # checks if the Task object is completed, if it is not, completed is set to True
        for i in range(len(tasks)):
            if self.task_name == tasks[i].name:
                tasks[i].completed = True
        print("The task was marked as complete if the right name was given. Nothing happened if the task name does not exist or was entered incorrectly.\n")
        
    def mark_as_incomplete(self) -> None: # sets the Task object's completed attribute to False
        for i in range(len(tasks)):
            if self.task_name == tasks[i].name:
                tasks[i].completed = False
        print("The task was marked as incomplete if the right name was given. Nothing happened if the task name does not exist or was entered incorrectly.\n")

    def add_task(self) -> None: # appends the Tasks object to a list of tasks
        tasks.append(self.task_name)
        
    def view_task(self) -> None: # finds a Task in a list of Task objects by name and then returns all of its metadata
        found_task = []
        for i in range(len(tasks)):
            if self.task_name == tasks[i].name:
                found_task.append(tasks[i])
                break
        if len(found_task) == 1:
            print("\nThe details of this task are as follows:\n")
            print(str(found_task[0]))
        else:
            print("\nThere are no tasks with this name!")
        found_task = []
    
    def remove_task(self) -> None: # checks if the Task object exists in the tasks list, then removes it from the list if it does exist
        for x in range(len(tasks)): # Supposed to be a function that takes a list of Task objects and removes the ones that the user wants to remove
            if self.task_name == tasks[x].name:
                tasks.remove(tasks[x])
                break

    def view_completed_tasks(self) -> None: #checks if the Task objects are completed, and appends them to a new list if they are completed, and prints the new list
        complete_tasks = []
        for j in range(len(tasks)):
            if tasks[j].completed == True:
                complete_tasks.append(tasks[j])
        if len(complete_tasks) == 0:
            print("\nThere are no completed tasks.")
        for x in range(len(complete_tasks)):
            print("\n" + complete_tasks[x].name)
        complete_tasks = []

    def view_incomplete_tasks(self) -> None: # checks if the Task objects in a list are not completed, and appends those incomplete tasks to a new list that is printed
        incomplete_tasks = []
        for j in range(len(tasks)):
            if tasks[j].completed == False:
                incomplete_tasks.append(tasks[j])
        if len(incomplete_tasks) == 0:
            print("\nThere are no incomplete tasks.")
        for x in range(len(incomplete_tasks)):
            print("\n" + incomplete_tasks[x].name)
        incomplete_tasks = []

    def view_category(self) -> None: # checks the tasks list for Task objects that have the same category, and appends those tasks to a new list that is printed
        category_tasks = []
        for j in range(len(tasks)):
            if tasks[j].category == self.task_name:
                category_tasks.append(tasks[j])
        if len(category_tasks) == 0:
            print("There are no tasks in this category.")
        for x in range(len(category_tasks)):
            print("\n" + category_tasks[x].name)
        category_tasks = []
