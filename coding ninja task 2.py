from expense_tracker import Expense
import calendar
import datetime


def main():
    print(f"Running Expense Tracker")
    expense_file_path = "expenses.csv"
    budget = 2000

    # User input
    expense = get_user_expense()

    # put in a file
    save_expense_to_file(expense, expense_file_path)

    # Read and Summarise the expenses
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print(f"😘Getting User Experience")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "🍉Food",
        "🏠Home",
        "🏢Work",
        "🎉Fun",
        "🚴Misc",
    ]

    while True:
        print("Select a Category : ")
        for i, category_name in enumerate(expense_categories):
            print(f"   {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a Category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid Category . Please try again!")


def save_expense_to_file(expense, expense_file_path):
    print(f"🎯Saving User Experience : {expense} to {expense_file_path}")
    with open(expense_file_path, mode='a', encoding='utf-8') as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")


def summarize_expenses(expense_file_path: object, budget, stripped_line: object = None) -> object:
    print("💕 Summarizing User Expenses")
    expenses = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category)

            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")

    total_spent = sum([ex.amount for ex in expenses])
    print(f"you've spent ${total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"✅Budget remaining ${remaining_budget:.2f} this month!")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉Budget Per Day: ${daily_budget:.2f}"))


def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()
