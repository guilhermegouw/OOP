import sys

from to_do_list import ToDoList


class Menu:
    """
    Display a menu and respond to choices when run.
    """

    def __init__(self) -> None:
        self.to_do_list = ToDoList()
        self.choices = {
            "1": self.show_tasks,
            "2": self.search_tasks,
            "3": self.add_task,
            "4": self.update_task,
            "5": self.quit,
        }

    def display_menu(self):
        """
        Display the menu
        """
        print(
            """
            To-Do-LIst Menu
            1. Show all Tasks
            2. Search Task
            3. Add Task
            4. Modify Task
            5. Quit
            """
        )

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice.")

    def show_tasks(self, task=None):
        if not task:
            tasks = self.to_do_list.tasks
        for task in tasks:
            print(f"{task.id}: {task.tag}\n{task.content}")

    def search_tasks(self):
        filter = input("Search for: ")
        tasks = self.to_do_list.search(filter)
        self.show_notes(tasks)

    def add_task(self):
        content = input("Enter a content: ")
        self.to_do_list.new_task(content)
        print("Your task has been added")

    def update_task(self):
        id = input("Enter a task id: ")
        content = input("Enter a content: ")
        tag = input("Enter a tag: ")
        if content:
            self.to_do_list.update_task(id, content)
        if tag:
            self.to_do_list.update_tag(id, tag)

    def quit(self):
        print("Thank you for using your To-Do-List today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
