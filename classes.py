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

    def __repr__(self) -> str:
        return "The name of the task is: \"{}\"\nThe description is: \"{}\"\nThe due-date is: {}\nThe category of task is: \"{}\"\nThe time of day it is due is: {}\nIs the task completed?: {}\nThe location of the task is: \"{}\"".format(self.name, self.description, self.due_date, self.category, self.time, self.completed, self.location)

    def mark_as_complete(self):
        self.completed = True

    def get_status(self):
        if self.completed:
            print("Status: Completed")
        else:
            print("Status: In progress")


class TodoList:
    def __init__(self, task: Task):
        self.task = task

    def __str__(self):
        return "Task: {}".format(self.task)

    def __repr__(self):
        return "To-do list {}".format(self.task)

    def add_task(self):
        tasks.append(self.task)

    def remove_task(self):
        updated_tasks = []
        if self.task in tasks:
            for i in tasks:
                if self.task not in i:
                    updated_tasks.append(i)

    def view_tasks(self)->list[Task]:
        for i in range(1, len(tasks)):
            temp = tasks[i]
            j = i - 1
            while j >= 0 and temp.due_date < tasks[j].due_date:
                tasks[j + 1] = tasks[j]
                j -= 1
            tasks[j + 1] = temp
        return tasks

    def view_completed_tasks(self, tasks:list[Task])->list[Task]:
        updated_tasks = []
        for i in range(1, len(tasks)):
            temp = tasks[i]
            j = i - 1
            while j >= 0 and temp.due_date < tasks[j].due_date:
                tasks[j + 1] = tasks[j]
                j -= 1
            tasks[j + 1] = temp
        for j in tasks:
            if tasks[j].completed:
                updated_tasks.append(tasks[j])
        return updated_tasks

    def view_incomplete_tasks(self, tasks:list[Task])->list[Task]:
        updated_tasks = []
        for i in range(1, len(tasks)):
            temp = tasks[i]
            j = i - 1
            while j >= 0 and temp.due_date < tasks[j].due_date:
                tasks[j + 1] = tasks[j]
                j -= 1
            tasks[j + 1] = temp
        for j in tasks:
            if tasks[j].completed == False:
                updated_tasks.append(tasks[j])
        return updated_tasks

    def view_category(self, tasks:list[Task], category:str)->list[Task]:
        updated_tasks = []
        for task in tasks:
            if task.category == category:
                updated_tasks.append(task)
        return updated_tasks


