import json
import os

users_file = "users.json"


def load_func():
    if os.path.exists(users_file):
        with open(users_file, "r") as r:
            return json.load(r)
    return {}

def save_func(users):
    with open(users_file, "w") as w:
        json.dump(users, w, indent=2)

def is_valid_email(email):
    return email.endswith("@domain") and len(email) > len("@domain")

def register_func(email, password, display_name, currency, monthly_income):
    users = load_func()

    if not is_valid_email(email):
        raise ValueError("Email must end with @domain.")
    
    elif email in users:
        raise ValueError("Account already exists.")

    users[email] = {
        "password": password, "display name": display_name,
        "currency": currency, "monthly income": float(monthly_income)
    }

    save_func(users)
    return "Registered successfully."


def login(email, password):
    users = load_func()
    if email not in users:
        return False, "Wrong Email, Try Again."
    if users[email]["password"] == password:
        return True, f"Welcome, {users[email]['display_name']}!"
    return False, "Invalid password."


def get_profile(email):
    users = load_func()
    return users.get(email)

def update_profile(email, display_name, currency, monthly_income):
    users = load_func()
    if email not in users:
        return False, "User not found."
    users[email]["display_name"] = display_name
    users[email]["currency"] = currency
    users[email]["monthly_income"] = float(monthly_income)
    save_func(users)
    return True, "Profile updated."
