from models.task import Task
from models.project import Project
from models.user import User

import argparse
import sys

users = {}
projects = {}

def add_task(args):
    user = users.get(args.username)
    if not user:
        user = User(args.username, args.email)
        users[args.username] = user
    task = Task(args.title, args.status, args.due_date, user)
    project = projects.get(args.project_name)
    if not project:
        project = Project(args.project_name, args.due_date)
        projects[args.project_name] = project
    project.add_task(task)

def list_tasks(args):
    project = projects.get(args.project_name)
    if project:
        tasks = project.list_tasks()
        for task in tasks:
            print(task)
    else:
        print(f"Project '{args.project_name}' not found.")

parser = argparse.ArgumentParser(description="Task Management System")
subparsers = parser.add_subparsers()

#add task command
add_parser = subparsers.add_parser("add_task", help="Add a new task to a project")
add_parser.add_argument("title", type=str, help="Title of the task")
add_parser.add_argument("status", type=str, help="Status of the task")
add_parser.add_argument("due_date", type=str, help="Due date of the task")
add_parser.add_argument("username", type=str, help="Username of the user to assign the task to")
add_parser.add_argument("email", type=str, help="Email of the user to assign the task to")
add_parser.add_argument("project_name", type=str, help="Name of the project to add the task to")
add_parser.set_defaults(func=add_task)

#list tasks command
list_parser = subparsers.add_parser("list_tasks", help="List all tasks in a project")
list_parser.add_argument("project_name", type=str, help="Name of the project to list tasks for")
list_parser.set_defaults(func=list_tasks)



if __name__ == "__main__":
    # Example usage
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args) 
    else:
        parser.print_help()
