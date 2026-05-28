import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!\n")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.\n")
        return

    print("\nAll Expenses:\n")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. "
            f"{expense['name']} | "
            f"₹{expense['amount']} | "
            f"{expense['category']}"
        )

    print()


def total_spending(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Spending: ₹{total}\n")


def category_spending(expenses):
    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        categories[category] = categories.get(category, 0) + amount

    print("\nCategory-wise Spending:\n")

    for category, total in categories.items():
        print(f"{category}: ₹{total}")

    print()


def main():
    expenses = load_expenses()

    while True:
        print("===== SMART EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category Spending")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_spending(expenses)

        elif choice == "4":
            category_spending(expenses)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
