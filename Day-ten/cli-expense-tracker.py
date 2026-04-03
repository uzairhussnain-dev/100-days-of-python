import json

FILE = "expenses.json"

def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_expenses(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(data):
    desc = input("Enter description: ")
    amount = float(input("Enter amount: "))

    data.append({"desc": desc, "amount": amount})
    save_expenses(data)

    print("✅ Expense added!")

def view_expenses(data):
    total = 0

    print("\n📋 Expenses:")
    for i, exp in enumerate(data, 1):
        print(f"{i}. {exp['desc']} - {exp['amount']}")
        total += exp["amount"]

    print(f"\n💰 Total: {total}")

def main():
    data = load_expenses()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()