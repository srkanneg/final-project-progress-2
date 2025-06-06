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


def remove_task(task_name, task_list):
    return [task for task in task_list if task.name != task_name]


def view_completed_tasks(task_list):
    return [task.name for task in task_list if task.completed]


def view_incomplete_tasks(task_list):
    return [task.name for task in task_list if not task.completed]


def view_category(category, task_list):
    result = [task.name for task in task_list if task.category == category]
    return result or ["There are no tasks in this category."]
