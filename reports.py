import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from tabulate import tabulate
from database import DB_NAME

def load_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    return df

def show_summary():
    df = load_data()
    if df.empty:
        print("No data available.")
        return
    total_income = df[df["amount"] > 0]["amount"].sum()
    total_expenses = df[df["amount"] < 0]["amount"].sum()
    net_balance = total_income + total_expenses

    print("\n--- Summary ---")
    print(f"Total Income: ₹ {total_income:.2f}")
    print(f"Total Expenses: ₹ {abs(total_expenses):.2f}")
    print(f"Net Balance: ₹ {net_balance:.2f}")

def show_category_report():
    df = load_data()
    if df.empty:
        print("No data available.")
        return
    category_totals = df.groupby("category")["amount"].sum()
    print("\n--- Category Report ---")
    print(tabulate(category_totals.reset_index(), headers=["Category", "Amount"], tablefmt="grid"))

def plot_expenses_by_category():
    df = load_data()
    if df.empty:
        print("No data available.")
        return
    expenses = df[df["amount"] < 0]
    if expenses.empty:
        print("No expenses to plot.")
        return
    category_totals = expenses.groupby("category")["amount"].sum().abs()
    category_totals.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Expenses by Category")
    plt.ylabel("")
    plt.show()

def plot_monthly_trend():
    df = load_data()
    if df.empty:
        print("No data available.")
        return
    df["date"] = pd.to_datetime(df["date"])
    monthly_totals = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()
    monthly_totals.plot(kind="bar")
    plt.title("Monthly Net Balance Trend")
    plt.xlabel("Month")
    plt.ylabel("Net Balance (₹)")
    plt.show()
