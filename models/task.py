
class Task:
    def __init__(self, title, status, assigned_to):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to

    def __repr__(self):
        return f"Task: {self.title}, Status: {self.status}, Assigned to: {self.assigned_to}"

    def update_status(self, new_status):
        self.status = new_status
        print(f"Task '{self.title}' status updated to '{self.status}'.")

    def assign_to(self, user):
        self.assigned_to = user
        print(f"Task '{self.title}' assigned to user '{user.username}'.")