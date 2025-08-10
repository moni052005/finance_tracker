from database import init_db, add_transaction, get_all_transactions
from reports import show_summary, show_category_report, plot_expenses_by_category, plot_monthly_trend
from tabulate import tabulate

def main():
    init_db()
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Summary")
        print("4. Show Category Report")
        print("5. Plot Expenses by Category")
        print("6. Plot Monthly Trend")
        print("7. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount (positive for income, negative for expense): "))
            add_transaction(date, category, description, amount)
            print("Transaction added successfully.")
        
        elif choice == "2":
            rows = get_all_transactions()
            if rows:
                print(tabulate(rows, headers=["ID", "Date", "Category", "Description", "Amount"], tablefmt="grid"))
            else:
                print("No transactions found.")
        
        elif choice == "3":
            show_summary()
        
        elif choice == "4":
            show_category_report()
        
        elif choice == "5":
            plot_expenses_by_category()
        
        elif choice == "6":
            plot_monthly_trend()
        
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
