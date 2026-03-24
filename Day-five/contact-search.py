contacts = {
    "Ali": "123456789",
    "Ahmed": "987654321",
    "Sara": "555666777"
}

def search_contact():
    name = input("Enter name to search: ").capitalize()

    if name in contacts:
        print(f"📞 {name}'s number is {contacts[name]}")
    else:
        print("❌ Contact not found")

def add_contact():
    name = input("Enter name: ").capitalize()
    number = input("Enter number: ")

    contacts[name] = number
    print("✅ Contact added")

def show_contacts():
    print("\n📋 Contact List:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

def menu():
    while True:
        print("\n1. Search Contact")
        print("2. Add Contact")
        print("3. Show All Contacts")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            search_contact()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            show_contacts()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice")

menu()