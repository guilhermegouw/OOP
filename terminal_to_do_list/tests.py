import unittest

from to_do_list import Task, ToDoList


class TaskTests(unittest.TestCase):
    def setUp(self) -> None:
        self.task = Task("test task")

    def test_match_return_True(self):
        """Should return True since test is in 'test task'"""
        self.assertEqual(self.task.match("test"), True)

    def test_match_return_False(self):
        """Should return False since match is case-sensitive"""
        self.assertEqual(self.task.match("Test"), False)


class ToDoListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.todo_list = ToDoList()
        self.todo_list.tasks = [Task("test task")]
        self.todo_list.tasks[0].id = 1

    def test_search_will_find(self):
        """Should find since test is in 'test task'"""
        self.assertIn(self.todo_list.tasks[0], self.todo_list.search("test"))

    def test_search_will_not_find(self):
        """Should not find since Test is not in 'test task'"""
        self.assertNotIn(self.todo_list.tasks[0], self.todo_list.search("Test"))

    def test_new_task(self):
        self.todo_list.new_task("new task")
        self.assertEqual(self.todo_list.tasks[1].content, "new task")

    def test_update_task(self):
        self.todo_list.update_task(1, "modified task")
        self.assertEqual(self.todo_list.tasks[0].content, "modified task")

    def test_update_tag(self):
        self.todo_list.update_tag(1, "new tag")
        self.assertEqual(self.todo_list.tasks[0].tag, "new tag")


if __name__ == "__main__":
    unittest.main()
