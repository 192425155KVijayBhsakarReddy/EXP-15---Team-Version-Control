"""
Module: Task & Milestone Tracker
Author: Team Member 3
Experiment: 15 (Version Control & Collaboration)
"""

tasks = [
    {"task_id": "TASK-101", "title": "Setup Docker container", "assignee": "lead_dev", "status": "In Progress"},
    {"task_id": "TASK-102", "title": "Implement unit testing", "assignee": "qa_tester", "status": "To Do"},
    {"task_id": "TASK-103", "title": "Configure GitHub Actions", "assignee": "admin", "status": "Done"}
]

def get_tasks_by_assignee(username):
    return [t for t in tasks if t["assignee"] == username]

def update_task_status(task_id, new_status):
    for t in tasks:
        if t["task_id"] == task_id:
            t["status"] = new_status
            return True
    return False
