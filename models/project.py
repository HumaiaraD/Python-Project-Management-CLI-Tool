
class Project:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added to project '{self.name}'.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task.title}' removed from project '{self.name}'.")

    def list_tasks(self):
        print(f"Listing tasks for project '{self.name}':")
        for task in self.tasks:
            print(f" - {task.title}")
        return self.tasks

    def __repr__(self):
        return f"Project: {self.name}, Description: {self.description}, Due Date: {self.due_date}, Tasks: {len(self.tasks)}"

    
