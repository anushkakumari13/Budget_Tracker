from expense import Expense


def main():
    print("Running expense Tracker!")
    expense_file_path = "expenses.csv"
    #budget = 15400
    budget = float(input("Enter your budget :"))
    print(f"You have entered budget: ${budget} ")

    #Get user input for expense.
    expense = get_user_expense()
    
    #Write that expense to a file.
    save_expense_to_file(expense, expense_file_path)

    #Read file and summarize expenses.
    summarize_expenses(expense_file_path, budget)

    
def get_user_expense():
    print("Getting User Expense ")
    expense_name = input(" Enter expense name: ")
    expense_amount = input(" Enter expense amount: ")    
    expense_categories = [
        "  Food",
        "  Home",
        "  Work",
        "  Fun",
        "  Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
        
        if i in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                 name = expense_name, category = selected_category, amount = expense_amount
                )
            return new_expense
        else:
            print("Invalid category. Please try again !!")
  
            
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expenses(expense_file_path, budget):
    print("Summarizing User Expense ")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            #print(expense_name, expense_amount, expense_category)
            line_expense = Expense(
                name = expense_name, amount = float(expense_amount), category = expense_category
            )
            print(line_expense)
            expenses.append(line_expense)
        #print(expenses)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses by Category: ")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You have spent ${total_spent}")

    remaining_budget = budget - total_spent

    if remaining_budget<=0:
        print("You donot have enough budget")

    else:
        print(f"Budget remaining ${remaining_budget}")

            
if __name__ == "__main__":
    main()
