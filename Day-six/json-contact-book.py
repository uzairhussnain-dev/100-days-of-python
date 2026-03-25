import json

FILE_NAME = "contacts.json"

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").capitalize()
    number = input("Enter number: ")

    contacts[name] = number
    save_contacts(contacts)
    print("✅ Contact saved!")

def view_contacts(contacts):
    print("\n📋 Contacts:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

def search_contact(contacts):
    name = input("Enter name: ").capitalize()

    if name in contacts:
        print(f"📞 {name}: {contacts[name]}")
    else:
        print("❌ Not found")

def delete_contact(contacts):
    name = input("Enter name to delete: ").capitalize()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("❌ Deleted")
    else:
        print("Not found")

def main():
    contacts = load_contacts()

    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

main()