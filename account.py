import json
import os

users_file = "users.json"


def load_users():
    if os.path.exists(users_file):
        with open(users_file, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(users_file, "w") as f:
        json.dump(users, f, indent=2)

def is_valid_email(email):
    return email.endswith("@domain") and len(email) > len("@domain")

def register(email, password, display_name, currency, monthly_income):
    users = load_users()
    if not is_valid_email(email):
        return False, "Email must end with @domain."
    if email in users:
        return False, "Account already exists."

    users[email] = {
        "password": password,
        "display_name": display_name,
        "currency": currency,
        "monthly_income": float(monthly_income)
    }
    save_users(users)
    return True, "Registered successfully."

def login(email, password):
    users = load_users()
    if not is_valid_email(email):
        return False, "Wrong email! Must end with @domain."
    user = users.get(email)
    if user and user["password"] == password:
        return True, f"Welcome, {user['display_name']}!"
    return False, "Invalid email or password."

def login(email, password):
    users = load_users()
    if email not in users:
        return False, "Wrong Email, Try Again."
    if users[email]["password"] == password:
        return True, f"Welcome, {users[email]['display_name']}!"
    return False, "Invalid password."


def get_profile(email):
    users = load_users()
    return users.get(email)

def update_profile(email, display_name, currency, monthly_income):
    users = load_users()
    if email not in users:
        return False, "User not found."
    users[email]["display_name"] = display_name
    users[email]["currency"] = currency
    users[email]["monthly_income"] = float(monthly_income)
    save_users(users)
    return True, "Profile updated."
