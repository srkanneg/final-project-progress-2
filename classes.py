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
    def __init__(self):
        self.tasks = []

    def __str__(self):
        result = ""
        for task in self.tasks:
            result += str(task) + "\n"
        return result

    def __repr__(self):
        return "To-do list {}".format(len(self.tasks))

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)

    def view_tasks(self) -> list[Task]:
        sorted_tasks = self.tasks.copy()
        for i in range(1, len(sorted_tasks)):
            temp = sorted_tasks[i]
            j = i - 1
            while j >= 0 and temp.due_date < sorted_tasks[j].due_date:
                sorted_tasks[j + 1] = sorted_tasks[j]
                j -= 1
            sorted_tasks[j + 1] = temp
        return sorted_tasks

    def view_completed_tasks(self) -> list[Task]:
        sorted_tasks = self.view_tasks()
        return [task for task in sorted_tasks if task.completed]

    def view_incomplete_tasks(self) -> list[Task]:
        sorted_tasks = self.view_tasks()
        return [task for task in sorted_tasks if not task.completed]

    def view_category(self, category: str) -> list[Task]:
        return [task for task in self.tasks if task.category == category]


