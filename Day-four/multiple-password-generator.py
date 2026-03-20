import random
import string

def generate_passwords():
    length = int(input("Enter password length: "))
    count = int(input("How many passwords to generate: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    print("\n🔐 Generated Passwords:\n")

    for _ in range(count):
        password = ''.join(random.choice(characters) for _ in range(length))
        print(password)

generate_passwords()