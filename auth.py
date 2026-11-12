"""
Module: Authentication & Session Management
Author: Team Member 1
Experiment: 15 (Version Control & Collaboration)
"""

def authenticate_user(username, password):
    # Simulated authentication database
    credentials = {
        "admin": "SuperAdminPass2026",
        "lead_dev": "DevSecure!99",
        "qa_tester": "TestPassed#12"
    }
    
    if username in credentials and credentials[username] == password:
        return {
            "success": True,
            "token": f"jwt_mock_token_{username}_valid",
            "role": "admin" if username == "admin" else "contributor"
        }
    return {
        "success": False,
        "error": "Invalid username or password"
    }

def verify_token(token):
    return token.startswith("jwt_mock_token_")
