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

- **Python 3** (no external libraries needed)
- **SQLite** via Python's built-in `sqlite3` module
- `csv` and `datetime` from the standard library

## How to Run

1. Install [Python 3](https://www.python.org/downloads/)
2. Clone this repo:
   ```
   git clone https://github.com/YOUR-USERNAME/expense-tracker.git
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

- Working with a relational database (creating tables, inserting, querying, grouping, deleting)
- Using parameterized queries (`?`) to avoid SQL injection
- Validating user input with loops and `try/except`
- Structuring a program into small, single-purpose functions

## Future Improvements

- Monthly budgets with warnings
- Edit existing expenses
- Charts using matplotlib
- A simple GUI or web version
