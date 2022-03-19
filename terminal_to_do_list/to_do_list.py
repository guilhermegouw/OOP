import datetime

current_id = 0


class Task:
    def __init__(self, content: str, tag: str = "") -> None:
        global current_id
        current_id += 1
        self.id = current_id
        self.content = content
        self.tag = tag
        self.created_at = datetime.date.today()

    def match(self, filter: str) -> bool:
        """Check if filter match task content or tag

        Args:
            filter (str): filter
        Returns:
            bool: True if filter matches part of the content or tag.
        """
        return filter in self.content or filter in self.tag


class ToDoList:
    def __init__(self) -> None:
        self.tasks = []

    def search(self, filter: str) -> list:
        return [task for task in self.tasks if task.match(filter)]

    def new_task(self, content: str) -> None:
        """Add a new task with the given content to tasks list"""
        self.tasks.append(Task(content))

    def _find_task(self, task_id):
        for task in self.tasks:
            if str(task.id) == str(task_id):
                return task
            else:
                print("Task not found")

    def update_task(self, task_id: int, new_content: str) -> None:
        """Update task content to the given new_content"""
        if self._find_task(task_id):
            self._find_task(task_id).content = new_content
        else:
            None

    def update_tag(self, task_id: int, new_tag: str) -> None:
        """Update task tag ro the given new_tag"""
        if self._find_task(task_id):
            self._find_task(task_id).tag = new_tag
        else:
            None
