

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.projects = []

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

    def add_project(self, project):
        self.projects.append(project)
        print(f"Project '{project.name}' added to user '{self.username}'.")

    def list_projects(self):
        return self.projects

    