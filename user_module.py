"""
Module: User Profile Management
Author: Team Member 2
Experiment: 15 (Version Control & Collaboration)
"""

users_db = [
    {"id": 1, "username": "admin", "full_name": "System Administrator", "dept": "IT Security"},
    {"id": 2, "username": "lead_dev", "full_name": "Sarah Connor", "dept": "Engineering"},
    {"id": 3, "username": "qa_tester", "full_name": "John Doe", "dept": "Quality Assurance"}
]

def get_user_by_id(user_id):
    for user in users_db:
        if user["id"] == user_id:
            return user
    return None

def list_all_users():
    return users_db
