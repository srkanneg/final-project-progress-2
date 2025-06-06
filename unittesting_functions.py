import unittest
from classes import Task
from test_helpers import (
    get_status,
    mark_as_complete,
    mark_as_incomplete,
    add_task,
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

    def test_get_status_completed(self):
        tasks = [Task("A", "", "", "", "", True, "")]
        self.assertEqual(get_status("A", tasks), "Status: Completed")

    def test_get_status_in_progress(self):
        tasks = [Task("A", "", "", "", "", False, "")]
        self.assertEqual(get_status("A", tasks), "Status: In Progress")

    def test_get_status_multiple(self):
        tasks = [
            Task("A", "", "", "", "", True, ""),
            Task("A", "", "", "", "", True, "")
        ]
        self.assertEqual(
            get_status("A", tasks),
            "Something went wrong, please reach out to the developers."
        )

    def test_mark_as_complete(self):
        task = Task("A", "", "", "", "", False, "")
        mark_as_complete("A", [task])
        self.assertTrue(task.completed)

    def test_mark_as_incomplete(self):
        task = Task("A", "", "", "", "", True, "")
        mark_as_incomplete("A", [task])
        self.assertFalse(task.completed)

    def test_add_task(self):
        tasks = []
        new_task = Task("B", "", "", "", "", False, "")
        add_task(new_task, tasks)
        self.assertIn(new_task, tasks)

    def test_remove_task(self):
        task1 = Task("A", "", "", "", "", False, "")
        task2 = Task("B", "", "", "", "", False, "")
        tasks = [task1, task2]
        updated = remove_task("A", tasks)
        self.assertEqual(len(updated), 1)
        self.assertEqual(updated[0].name, "B")

    def test_view_completed_tasks(self):
        tasks = [
            Task("A", "", "", "", "", True, ""),
            Task("B", "", "", "", "", False, "")
        ]
        result = view_completed_tasks(tasks)
        self.assertEqual(result, ["A"])

    def test_view_incomplete_tasks(self):
        tasks = [
            Task("A", "", "", "", "", False, ""),
            Task("B", "", "", "", "", True, "")
        ]
        result = view_incomplete_tasks(tasks)
        self.assertEqual(result, ["A"])

    def test_view_category(self):
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

    def test_view_tasks(self):
        tasks = [
            Task("A", "", "2025-07-01", "School", "", False, ""),
            Task("B", "", "2025-06-01", "Work", "", False, "")
        ]
        result = view_tasks(tasks)
        self.assertEqual(result, ["B", "A"])

    def test_sort_due_date(self):
        tasks = [
            Task("A", "", "2025-07-01", "School", "", False, ""),
            Task("B", "", "2025-06-01", "Work", "", False, "")
        ]
        result = sort_due_date(tasks)
        self.assertEqual([t.name for t in result], ["B", "A"])

    def test_sort_cat_alpha(self):
        tasks = [
            Task("A", "", "2025-07-01", "School", "", False, ""),
            Task("B", "", "2025-06-01", "Work", "", False, "")
        ]
        result = sort_cat_alpha(tasks)
        self.assertEqual([t.category for t in result], ["School", "Work"])

    def test_print_list(self):
        tasks = [
            Task("A", "", "2025-07-01", "School", "", False, ""),
            Task("B", "", "2025-06-01", "Work", "", False, "")
        ]
        result = print_list(tasks)
        self.assertEqual(result, ["A", "B"])

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

    def test_view_categories2(self): # if tasks is empty
        tasks = []
        result = view_categories(tasks)
        self.assertEqual(result, ["There are no categories"])


if __name__ == '__main__':
    unittest.main()
