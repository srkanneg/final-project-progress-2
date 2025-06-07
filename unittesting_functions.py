# Jack is the author of this file

import unittest
from classes import Task
from test_helpers import (
    get_status,
    mark_as_complete,
    mark_as_incomplete,
    add_task,
    view_task,
    remove_task,
    view_completed_tasks,
    view_incomplete_tasks,
    view_category,
    view_tasks,
    sort_due_date,
    sort_cat_alpha,
    print_list,
    collect_categories,
    view_categories
)

class TestTaskHelpers(unittest.TestCase):

    def test_get_status_completed_1(self):
        tasks = [Task("A", "", "", "", "", True, "")]
        self.assertEqual(get_status("A", tasks), "Status: Completed")
    
    def test_get_status_completed_2(self):
        tasks = [Task("B", "", "", "", "", True, "")]
        self.assertEqual(get_status("B", tasks), "Status: Completed")

    def test_get_status_in_progress_1(self):
        tasks = [Task("A", "", "", "", "", False, "")]
        self.assertEqual(get_status("A", tasks), "Status: In Progress")
    
    def test_get_status_in_progress_2(self):
        tasks = [Task("B", "", "", "", "", False, "")]
        self.assertEqual(get_status("B", tasks), "Status: In Progress")

    def test_get_status_multiple(self):
        tasks = [
            Task("A", "", "", "", "", True, ""),
            Task("A", "", "", "", "", True, "")
        ]
        self.assertEqual(
            get_status("A", tasks),
            "Something went wrong, please reach out to the developers."
        )

    def test_mark_as_complete_1(self):
        task = Task("A", "", "", "", "", False, "")
        mark_as_complete("A", [task])
        self.assertTrue(task.completed)
        
    def test_mark_as_complete_2(self):
        task = Task("B", "", "", "", "", True, "")
        mark_as_complete("B", [task])
        self.assertTrue(task.completed)

    def test_mark_as_incomplete_1(self):
        task = Task("A", "", "", "", "", True, "")
        mark_as_incomplete("A", [task])
        self.assertFalse(task.completed)
        
    def test_mark_as_incomplete_2(self):
        task = Task("B", "", "", "", "", False, "")
        mark_as_incomplete("A", [task])
        self.assertFalse(task.completed)

    def test_add_task_1(self):
        tasks = []
        new_task = Task("B", "", "", "", "", False, "")
        add_task(new_task, tasks)
        self.assertIn(new_task, tasks)
        
    def test_add_task_2(self):
        tasks = []
        new_task = Task("A", "", "", "", "", False, "")
        add_task(new_task, tasks)
        self.assertIn(new_task, tasks)
    
    def test_view_task_1(self):
        tasks = [Task("A", "", "", "", "", False, "")]
        self.assertEqual(True, view_task("A", tasks))
        
    def test_view_task_2(self):
        tasks = [Task("A", "", "", "", "", False, "")]
        self.assertEqual(False, view_task("B", tasks))

    def test_remove_task_1(self):
        task1 = Task("A", "", "", "", "", False, "")
        task2 = Task("B", "", "", "", "", False, "")
        tasks = [task1, task2]
        updated = remove_task("A", tasks)
        self.assertEqual(len(updated), 1)
        self.assertEqual(updated[0].name, "B")
    
    def test_remove_task_2(self):
        task1 = Task("B", "", "", "", "", False, "")
        task2 = Task("A", "", "", "", "", False, "")
        tasks = [task1, task2]
        updated = remove_task("A", tasks)
        self.assertEqual(len(updated), 1)
        self.assertEqual(updated[0].name, "B")

    def test_view_completed_tasks_1(self):
        tasks = [
            Task("A", "", "", "", "", True, ""),
            Task("B", "", "", "", "", False, "")
        ]
        result = view_completed_tasks(tasks)
        self.assertEqual(result, ["A"])
        
    def test_view_completed_tasks_2(self):
        tasks = [
            Task("A", "", "", "", "", False, ""),
            Task("B", "", "", "", "", True, "")
        ]
        result = view_completed_tasks(tasks)
        self.assertEqual(result, ["B"])

    def test_view_incomplete_tasks_1(self):
        tasks = [
            Task("A", "", "", "", "", False, ""),
            Task("B", "", "", "", "", True, "")
        ]
        result = view_incomplete_tasks(tasks)
        self.assertEqual(result, ["A"])
        
    def test_view_incomplete_tasks_2(self):
        tasks = [
            Task("A", "", "", "", "", True, ""),
            Task("B", "", "", "", "", True, "")
        ]
        result = view_incomplete_tasks(tasks)
        self.assertEqual(result, [])

    def test_view_category_1_and_2(self):
        tasks = [
            Task("A", "", "", "School", "", False, ""),
            Task("B", "", "", "Work", "", False, "")
        ]
        # when category is found
        result = view_category("School", tasks)
        self.assertEqual(result, ["A"])
        # when category is not found
        result = view_category("Shopping", tasks)
        self.assertEqual(result, ["There are no tasks in this category."])

    def test_view_tasks_1(self):
        tasks = [
            Task("A", "", "2025-07-01", "School", "", False, ""),
            Task("B", "", "2025-06-01", "Work", "", False, "")
        ]
        result = view_tasks(tasks)
        self.assertEqual(result, ["B", "A"])
        
    def test_view_tasks_2(self):
        tasks = [
            Task("A", "", "2025-07-01", "School", "", False, ""),
            Task("B", "", "2025-08-01", "Work", "", False, "")
        ]
        result = view_tasks(tasks)
        self.assertEqual(result, ["A", "B"])

    def test_sort_due_date_1(self):
        tasks = [
            Task("A", "", "2025-07-01", "School", "", False, ""),
            Task("B", "", "2025-06-01", "Work", "", False, "")
        ]
        result = sort_due_date(tasks)
        self.assertEqual([t.name for t in result], ["B", "A"])
        
    def test_sort_due_date_2(self):
        tasks = [
            Task("A", "", "2025-07-01", "School", "", False, ""),
            Task("B", "", "2025-06-01", "Work", "", False, "")
        ]
        result = sort_due_date(tasks)
        self.assertEqual([t.name for t in result], ["B", "A"])

    def test_sort_cat_alpha_1(self):
        tasks = [
            Task("A", "", "2025-07-01", "School", "", False, ""),
            Task("B", "", "2025-06-01", "Work", "", False, "")
        ]
        result = sort_cat_alpha(tasks)
        self.assertEqual([t.category for t in result], ["School", "Work"])
    
    def test_sort_cat_alpha_2(self):
        tasks = [
            Task("D", "", "2025-07-01", "B", "", False, ""),
            Task("C", "", "2025-06-01", "A", "", False, "")
        ]
        result = sort_cat_alpha(tasks)
        self.assertEqual([t.category for t in result], ["A", "B"])

    def test_print_list_1(self):
        tasks = [
            Task("A", "", "2025-07-01", "School", "", False, ""),
            Task("B", "", "2025-06-01", "Work", "", False, "")
        ]
        result = print_list(tasks)
        self.assertEqual(result, ["A", "B"])
        
    def test_print_list_2(self):
        tasks = [
            Task("C", "", "2025-07-01", "School", "", False, ""),
            Task("D", "", "2025-06-01", "Work", "", False, "")
        ]
        result = print_list(tasks)
        self.assertEqual(result, ["C", "D"])

    def test_collect_categories(self):
        tasks = [
            Task("A", "", "2025-07-01", "School", "", False, ""),
            Task("B", "", "2025-06-01", "Work", "", False, "")
        ]
        result = collect_categories(tasks)
        self.assertEqual(set(result), {"School", "Work"})

    def test_view_categories(self):
        tasks = [
            Task("A", "", "2025-07-01", "School", "", False, ""),
            Task("B", "", "2025-06-01", "Work", "", False, "")
        ]
        result = view_categories(tasks)
        self.assertEqual(result, ["School", "Work"])

    def test_view_categories_2(self): # if tasks is empty
        tasks = []
        result = view_categories(tasks)
        self.assertEqual(result, ["There are no categories"])


if __name__ == '__main__':
    unittest.main()
