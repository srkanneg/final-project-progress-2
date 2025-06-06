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
    view_category
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


if __name__ == '__main__':
    unittest.main()
