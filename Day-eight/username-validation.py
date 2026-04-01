import re

def validate_username():
    username = input("Enter username: ")

    if len(username) < 3 or len(username) > 15:
        print("❌ Username must be 3–15 characters")
        return

    if not re.match(r"^[a-zA-Z0-9_]+$", username):
        print("❌ Only letters, numbers, and underscore allowed")
        return

    if username[0].isdigit():
        print("❌ Cannot start with a number")
        return

    print("✅ Valid username!")

validate_username()