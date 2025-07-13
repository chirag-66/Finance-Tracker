# Expense tracker (python CLI project)
A simple python command-line expense tracker that allows users to:
. Add income/expense transactions
. View and delete transaction 
. Export data to CSV
. Search and summarize transactions
. Clear all data from JSON or CSV files

# Features
. Add, view, delete, and search transactions
. Store transactions in JSON format
. Export transactions to CSV
. Delete all transactions in JSON
. Clear CSV file contents
. Simple command-line interface (CLI)
. Data persistence using local files

# Project Structure

Expense tracker/
|---data/
|    |---transactions.json
|    |---transactions.csv
|---models.py
|---tracker.py

. models.py -> Defines the Transaction class.
. tracker.py -> Main CLI logica and menu handling.
. data/ -> Contains transaction storage files.

# How to Run

1. Install Python 3
Make sure python 3 is installed on your system.

2.  Install Required Packages
You can install Colorama if it's not installed:
    pip install colorama

3. Run the Tracker
From your vs terminal:
python tracker.py

#Usage Menu Example
===== Expense Tracker =====
1. AddTransaction
2. View Transactions
3. Delete Transaction
4. View Summary
5. Search Transactions
6. Export to CSV
7. Delete All JSON Transactions
8. Clear CSV File
9. Exit

# Notes
1. Transactions are saved automatically in data/transactionsjson.
2. Exported CSV file: data/transactions.csv.
3. Deleting or clearing data is irreversible—use with care!