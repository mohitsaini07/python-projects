import datetime
import json
import os

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    else:
        return [
            {
                "date": "2026-09-15",
                "time": "12:40",
                "category": "Food",
                "amount": 250,
                "description": "Lunch"
            },
            {
                "date": "2026-09-15",
                "time": "08:45",
                "category": "Transport",
                "amount": 100,
                "description": "Bus"
            }
    ]

def save_expenses():
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

expenses = load_expenses()

def add_expense(date, time, category, price, description):
    expenses.append({
        "date": date,
        "time": time,
        "category": category,
        "amount": price,
        "description": description
    })
    save_expenses()
    print("Expense added successfully!")

def show_expense():
    if not expenses:
        print("No Expenses Found!")
    else:
        print("\nHere is your Expense List: \n")
        for expense in expenses:
            print(f"Date: {expense['date']} | Time: {expense['time']} | Category: {expense['category']} | Amount: ₹{expense['amount']} | Desc: {expense['description']}")

def total_expense():
    total = sum(expense["amount"] for expense in expenses)
    return total

def fltr_by_category(category):
    return [expense for expense in expenses if expense["category"].lower() == category.lower()]

def show_menu():
    print("\n----- Expense Tracker -----")
    print("1. Add Expense")
    print("2. Show Expense")    
    print("3. Total Expense")
    print("4. Filter by Category")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def run_app():
    while True:
        choice = show_menu()
        if choice == "1":
            date = datetime.date.today().isoformat()
            time = datetime.datetime.now().strftime("%H:%M")
            category = input("Enter Category: ")
            while True:
                try:
                    amount = float(input(f"Enter amount: ₹"))
                    break
                except ValueError:
                    print("Invalid amount")
            description = input("Enter description: ")
            add_expense(date, time, category, amount, description)
        
        elif choice == "2":
            show_expense()
        elif choice == "3":
            total = total_expense()
            print(f"Total Expenses: ")
        elif choice == "4":
            category = input("Enter a category: ")
            filtered = fltr_by_category(category)
            if not filtered:
                print("No expenses found in this category")
            else:
                print(f"\n--- {category} expenses ---")
                for expense in filtered:
                    print(f"Date: {expense['date']} | Time: {expense['time']} | Amount: ₹{expense['amount']} | Desc: {expense['description']}")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    run_app()

        


