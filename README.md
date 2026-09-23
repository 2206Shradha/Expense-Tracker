# Expense Tracker

A command-line expense tracker built with Python and SQLite. Add expenses, browse them, and see where your money goes, all stored locally in a database file.

## Features

- Add expenses with a date, category, description, and amount
- View all expenses in a formatted table
- Delete expenses by ID
- Spending summary by category, with percentages
- Monthly totals
- Export all data to CSV (opens in Excel / Google Sheets)
- Input validation for dates and amounts

## Tech Used

- **Python 3**
- **SQLite** via Python's built-in `sqlite3` module 
- `csv` and `datetime` from the standard library

## How to Run

1. Install [Python 3](https://www.python.org/downloads/)
2. Clone this repo:
   ```
   git clone https://github.com/2206Shradha/expense-tracker.git
   cd expense-tracker
   ```
3. Run it:
   ```
   python expense_tracker.py
   ```

The database file (`expenses.db`) is created automatically on first run.

## Example

```
===== EXPENSE TRACKER =====
1. Add expense
2. View all expenses
...
Choose an option: 4

--- Spending by Category ---
Food               245.50  (49.1%)
Rent               200.00  (40.0%)
Travel              54.50  (10.9%)
-----------------------------------
Total              500.00
```

## What I Learned

- Learned how to work with a database and perform basic operations like adding, viewing, and deleting expenses.
- Learned how to check user input and handle errors using loops and try/except.
- Learned how to break the program into smaller functions instead of putting everything in one place.

## Future Improvements

- Add monthly budgets and warnings when spending gets too high.
- Add an option to edit expenses.
- Maybe make a basic GUI or web version later.
