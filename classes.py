tasks = []

class Task:
    def __init__(self, name, description, due_date, category, time, completed, location) -> None:
        self.name = name
        self.description = description
        self.due_date = due_date
        self.category = category
        self.time = time
        self.completed = completed
        self.location = location

    def __str__(self) -> str:
        return "The name of the task is: \"{}\"\nThe description is: \"{}\"\nThe due-date is: {}\nThe category of task is: \"{}\"\nThe time of day it is due is: {}\nIs the task completed?: {}\nThe location of the task is: \"{}\"".format(self.name, self.description, self.due_date, self.category, self.time, self.completed, self.location)

    # def __repr__(self) -> str:
    #     return "The name of the task is: \"{}\"\nThe description is: \"{}\"\nThe due-date is: {}\nThe category of task is: \"{}\"\nThe time of day it is due is: {}\nIs the task completed?: {}\nThe location of the task is: \"{}\"".format(self.name, self.description, self.due_date, self.category, self.time, self.completed, self.location)



class TodoList:
    def __init__(self, task_name: str = None):
        self.task_name = task_name
    
    def get_status(self):
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
    
    def mark_as_complete(self):
        for i in range(len(tasks)):
            if self.task_name == tasks[i].name:
                tasks[i].completed = True
        print("The task was marked as complete if the right name was given. Nothing happened if the task name does not exist or was entered incorrectly.\n")
        
    def mark_as_incomplete(self):
        for i in range(len(tasks)):
            if self.task_name == tasks[i].name:
                tasks[i].completed = False
        print("The task was marked as incomplete if the right name was given. Nothing happened if the task name does not exist or was entered incorrectly.\n")

    def add_task(self):
        tasks.append(self.task_name)
    
    def remove_task(self):
        for x in range(len(tasks)): # Supposed to be a function that takes a list of Task objects and removes the ones that the user wants to remove
            if self.task_name == tasks[x].name:
                tasks.remove(tasks[x])
                break

    def view_completed_tasks(self):
        complete_tasks = []
        for j in range(len(tasks)):
            if tasks[j].completed == True:
                complete_tasks.append(tasks[j])
        if len(complete_tasks) == 0:
            print("\nThere are no completed tasks.")
        for x in range(len(complete_tasks)):
            print("\n" + complete_tasks[x].name)
        complete_tasks = []

    def view_incomplete_tasks(self):
        incomplete_tasks = []
        for j in range(len(tasks)):
            if tasks[j].completed == False:
                incomplete_tasks.append(tasks[j])
        if len(incomplete_tasks) == 0:
            print("\nThere are no incomplete tasks.")
        for x in range(len(incomplete_tasks)):
            print("\n" + incomplete_tasks[x].name)
        incomplete_tasks = []

    def view_category(self):
        category_tasks = []
        for j in range(len(tasks)):
            if tasks[j].category == self.task_name:
                category_tasks.append(tasks[j])
        if len(category_tasks) == 0:
            print("There are no tasks in this category.")
        for x in range(len(category_tasks)):
            print("\n" + category_tasks[x].name)
        category_tasks = []
