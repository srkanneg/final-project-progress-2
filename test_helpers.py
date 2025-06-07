# Jack is the author of this file and this file houses functions only used for unit testing

import classes

def get_status(task_name, task_list):
    matching_tasks = [task for task in task_list if task.name == task_name and task.completed]
    if len(matching_tasks) == 1:
        return "Status: Completed"
    elif len(matching_tasks) == 0:
        return "Status: In Progress"
    else:
        return "Something went wrong, please reach out to the developers."


def mark_as_complete(task_name, task_list):
    for task in task_list:
        if task.name == task_name:
            task.completed = True
    return task_list


def mark_as_incomplete(task_name, task_list):
    for task in task_list:
        if task.name == task_name:
            task.completed = False
    return task_list


def add_task(new_task, task_list):
    task_list.append(new_task)
    return task_list

def view_task(task_name, task_list):
    y = True
    for i in range(len(task_list)):
        if task_name == task_list[i].name:
            y = True
            break
        else:
            y = False
            break
    return y
        

def remove_task(task_name, task_list):
    return [task for task in task_list if task.name != task_name]


def view_completed_tasks(task_list):
    return [task.name for task in task_list if task.completed]


def view_incomplete_tasks(task_list):
    return [task.name for task in task_list if not task.completed]


def view_category(category, task_list):
    result = [task.name for task in task_list if task.category == category]
    return result or ["There are no tasks in this category."]


def sort_due_date(task_list):
    for i in range(1, len(task_list)):
        temp = task_list[i]
        j = i - 1
        while j >= 0 and temp.due_date < task_list[j].due_date:
            task_list[j + 1] = task_list[j]
            j -= 1
        task_list[j + 1] = temp
    return task_list


def sort_cat_alpha(task_list):
    for i in range(1, len(task_list)):
        temp = task_list[i]
        j = i - 1
        while j >= 0 and temp.category < task_list[j].category:
            task_list[j + 1] = task_list[j]
            j -= 1
        task_list[j + 1] = temp
    return task_list


def print_list(task_list):
    return [task.name for task in task_list]


def view_tasks(task_list):
    if not task_list:
        return ["Empty"]
    sorted_list = sort_due_date(task_list.copy())
    return print_list(sorted_list)


def collect_categories(task_list):
    categories = []
    for task in task_list:
        if task.category not in categories:
            categories.append(task.category)
    return categories


def view_categories(task_list):
    if not task_list:
        return ["There are no categories"]
    sorted_list = sort_cat_alpha(task_list.copy())
    return collect_categories(sorted_list)
