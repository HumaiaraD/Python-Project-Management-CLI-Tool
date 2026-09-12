import json

def save_data_to_file(users, projects, filename):
    """Converts objects to dictionaries and saves them as JSON."""

    data = {
        "users": {},
        "projects": {}
    }

    for username, user in users.items():
        data["users"][username] = {
            "email": user.email,
            "projects": [project.name for project in user.projects]
        }

    for project_name, project in projects.items():
        data["projects"][project_name] = {
            "description": project.description,
            "due_date": project.due_date,
            "tasks": [
                {
                    "title": task.title,
                    "status": task.status,
                    "assigned_to": task.assigned_to.username
                }
                for task in project.tasks
            ]
        }

    with open(filename, "a", encoding="utf-8") as f:
        json.dump(data, f, indent=4)