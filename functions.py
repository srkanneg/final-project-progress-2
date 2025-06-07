# Sriyans is the author of this file

import classes

def view_tasks() -> None: # prints a sorted list of Task objects
    if len(classes.tasks) == 0:
        print("Empty\n")
    sort_due_date()
    print_list()

def sort_due_date() -> None:
    for i in range(1, len(classes.tasks)):  # Supposed to be a function that takes a list of Task objects and sorts it by due date in ascending order
        temp = classes.tasks[i]
        j = i - 1
        while j >= 0 and temp.due_date < classes.tasks[j].due_date:
            classes.tasks[j + 1] = classes.tasks[j]
            j -= 1
        classes.tasks[j + 1] = temp

def sort_cat_alpha() -> None: # sorts a list of Task objects based on their category, in alphabetical order
    for i in range(1, len(classes.tasks)):
        temp = classes.tasks[i]
        j = i - 1
        while j >= 0 and temp.category < classes.tasks[j].category:
            classes.tasks[j + 1] = classes.tasks[j]
            j -= 1
        classes.tasks[j + 1] = temp

def print_list(thing: list[classes.Task] = classes.tasks) -> None: # Supposed to be a function to print the name of each task in the to-do list given a list of Task objects
    for i in range(len(thing)):
        print(thing[i].name + "\n")
        
def collect_categories() -> list[str]: # loops through a list of Task objects and appends the category of each Task object to a new list, with no duplicates
    categories = []
    for i in range(len(classes.tasks)):
        if classes.tasks[i].category not in categories:
            categories.append(classes.tasks[i].category)
    return categories

def view_categories() -> None: # gets the categories of a list of Task objects and prints a sorted list of the categories
    if len(classes.tasks) == 0:
        print("There are no categories\n")
    sort_cat_alpha()
    lst = collect_categories()
    for i in range(len(lst)):
        print(lst[i] + "\n")