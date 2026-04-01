import re

def check_password():
    password = input("Enter password: ")

    score = 0

    if len(password) >= 6:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    if score <= 1:
        print("❌ Weak Password")
    elif score <= 3:
        print("⚠️ Medium Password")
    else:
        print("✅ Strong Password")

check_password()