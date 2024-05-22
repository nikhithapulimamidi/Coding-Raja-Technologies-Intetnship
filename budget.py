import os
import json
from datetime import datetime

DATA_FILE = 'budget_tracker.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {'income': [], 'expenses': []}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_income(data):
    amount = float(input("Enter income amount: "))
    category = input("Enter income category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    income_entry = {
        'amount': amount,
        'category': category,
        'date': date
    }
    data['income'].append(income_entry)
    save_data(data)
    print("Income added successfully!")

def add_expense(data):
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    expense_entry = {
        'amount': amount,
        'category': category,
        'date': date
    }
    data['expenses'].append(expense_entry)
    save_data(data)
    print("Expense added successfully!")

def calculate_budget(data):
    total_income = sum(entry['amount'] for entry in data['income'])
    total_expenses = sum(entry['amount'] for entry in data['expenses'])
    remaining_budget = total_income - total_expenses
    return total_income, total_expenses, remaining_budget

def analyze_expenses(data):
    category_totals = {}
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    return category_totals

def display_analysis(data):
    category_totals = analyze_expenses(data)
    print("\nExpense Analysis by Category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

def display_summary(data):
    total_income, total_expenses, remaining_budget = calculate_budget(data)
    print("\nBudget Summary:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

def main():
    data = load_data()

    while True:
        print("\nBudget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Budget Summary")
        print("4. Display Expense Analysis")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            display_summary(data)
        elif choice == '4':
            display_analysis(data)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
