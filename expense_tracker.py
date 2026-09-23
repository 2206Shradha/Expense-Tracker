# Expense tracker - simple project using Python and SQLite

import csv
import sqlite3
from datetime import date, datetime

DB_FILE = "expenses.db"


# ---------- Database ----------

def connect():
    # opens the database (if it doesnt already exist it makes it)
    conn = sqlite3.connect(DB_FILE)
    # makes the expenses table the first time we run
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            date        TEXT NOT NULL,
            category    TEXT NOT NULL,
            description TEXT,
            amount      REAL NOT NULL
        )
        """
    )
    conn.commit()
    return conn


# ---------- Input helpers ----------

def ask_amount():
    # keeps asking until user types a valid number
    while True:
        try:
            amount = float(input("Amount: "))
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a number, like 12.50")


def ask_date():
    # Enter = today's date, otherwise it must be YYYY-MM-DD
    while True:
        text = input("Date (YYYY-MM-DD, Enter for today): ").strip()
        if text == "":
            return date.today().isoformat()
        try:
            # checks that the date is in the correct right format
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Invalid date. Example: 2026-09-23")


# ---------- Features ----------

def add_expense(conn):
    print("\n--- Add Expense ---")
    when = ask_date()
    category = input("Category (e.g. Food, Rent, Travel): ").strip().title()
    description = input("Description: ").strip()
    amount = ask_amount()

    # save the new expense in the database
    conn.execute(
        "INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
        (when, category, description, amount),
    )
    conn.commit()
    print("Expense added!")


def view_expenses(conn):
    print("\n--- All Expenses ---")
    # get all expenses, keeping the newest first
    rows = conn.execute(
        "SELECT id, date, category, description, amount FROM expenses ORDER BY date DESC"
    ).fetchall()

    if not rows:
        print("No expenses yet.")
        return

    print(f"{'ID':<4} {'Date':<12} {'Category':<12} {'Description':<20} {'Amount':>8}")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<4} {row[1]:<12} {row[2]:<12} {row[3]:<20} {row[4]:>8.2f}")


def delete_expense(conn):
    print("\n--- Delete Expense ---")
    view_expenses(conn)
    try:
        expense_id = int(input("\nEnter the ID to delete (or 0 to cancel): "))
    except ValueError:
        print("Invalid ID.")
        return
    if expense_id == 0:
        return

    # delete the expense with this id
    cursor = conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("No expense with that ID.")
    else:
        print("Deleted.")


def category_summary(conn):
    print("\n--- Spending by Category ---")
    # add up the amounts for each category
    rows = conn.execute(
        "SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY SUM(amount) DESC"
    ).fetchall()

    if not rows:
        print("No expenses yet.")
        return

    total = sum(row[1] for row in rows)
    for category, amount in rows:
        percent = amount / total * 100
        print(f"{category:<15} {amount:>10.2f}  ({percent:.1f}%)")
    print("-" * 35)
    print(f"{'Total':<15} {total:>10.2f}")


def monthly_total(conn):
    print("\n--- Monthly Total ---")
    month = input("Month (YYYY-MM, Enter for this month): ").strip()
    if month == "":
        month = date.today().strftime("%Y-%m")

    # finds all dates starting with the month, like 2026-09
    result = conn.execute(
        "SELECT SUM(amount), COUNT(*) FROM expenses WHERE date LIKE ?",
        (month + "%",),
    ).fetchone()

    total, count = result
    if count == 0:
        print(f"No expenses found for {month}.")
    else:
        print(f"{month}: {total:.2f} across {count} expense(s)")


def export_csv(conn):
    print("\n--- Export to CSV ---")
    rows = conn.execute(
        "SELECT date, category, description, amount FROM expenses ORDER BY date"
    ).fetchall()

    if not rows:
        print("Nothing to export.")
        return

    with open("expenses_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Description", "Amount"])
        writer.writerows(rows)
    print(f"Exported {len(rows)} expenses to expenses_export.csv")


# ---------- Main menu ----------

def main():
    conn = connect()

    # menu will keep running until the user picks 7 
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Delete expense")
        print("4. Spending by category")
        print("5. Monthly total")
        print("6. Export to CSV")
        print("7. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(conn)
        elif choice == "2":
            view_expenses(conn)
        elif choice == "3":
            delete_expense(conn)
        elif choice == "4":
            category_summary(conn)
        elif choice == "5":
            monthly_total(conn)
        elif choice == "6":
            export_csv(conn)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

    conn.close()


if __name__ == "__main__":
    main()
