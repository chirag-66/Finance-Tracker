from models import Transaction
import json
import os
import re
from colorama import Fore, Style, init
init(autoreset=True)
import csv

DATA_FILE = "data/transactions.json"

def load_transactions():
    if not os.path.exists(DATA_FILE):    #to read existing data from JSON file
        return []
    
    with open(DATA_FILE,"r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
        

def save_transaction(transaction):
    transactions = load_transactions()
    transactions.append(transaction.to_dict())     #to write new data to JSON file

    with open(DATA_FILE,"w") as file:
        json.dump(transactions, file, indent=4)


print(Fore.LIGHTBLUE_EX + "Saved successfully.")


def add_transaction():
        type_ = input("Enter type (income/expense): ").strip().lower()
        amount = float(input("Enter amount: "))
        category = input("Enter category: ").strip()
        note = input("Enter note: ").strip()
        date = input("Enter Exactdate: ")
    
        
        if type_ not in ['income', 'expense']:
            print("Invalid type. Must be 'income' or 'expense'.")
            return
    
        transaction = Transaction(type_, amount, category, note, date)
        save_transaction(transaction)
        print(Fore.GREEN + "Transaction added successfully.")
    
def view_transaction():
        transactions = load_transactions()
        if not transactions:
            print(Fore.RED + Style.BRIGHT + "NO transactions found.")
            return
        
        for i, t in enumerate(transactions, start=1):
            print(f"\nTransaction {i}:")
            print(f" Id: {t['id']}")    # catching each value by it's key
            print(f" Type: {t['type']}")
            print(f" Amount: {t['amount']}")
            print(f" Category: {t['category']}")
            print(f" Note: {t['note']}")
            print(f" Date: {t['date']}")

    
def delete_transaction():
        transactions = load_transactions()
        if not transactions:
            print(Fore.RED + Style.BRIGHT + "No transactions to delete.")
            return 
        
        id_to_delete = input("Enter the Transaction ID to delete: ")
    
        new_transactions = [t for t in transactions if str(t["id"]) != id_to_delete]
    
        if len(new_transactions) == len(transactions):
            print(Fore.RED + Style.BRIGHT + "Transaction not found.")
        else:
            with open(DATA_FILE, "w") as file:
                json.dump(new_transactions, file, indent=4)
                print(Fore.GREEN + "Transaction deleted.")
    
def show_summary():
        transactions = load_transactions()
    
        total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
        total_expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
        balance = total_income - total_expense
    
        print("\n===== Summary =====")
        print(f"Total Income : rup{total_income}")
        print(f"Total Expense : rup{total_expense}")
        print(f"Balance : rup{balance}")
    
def search_transactions():
        transactions = load_transactions()
        if not transactions:
            print(Fore.RED + Style.BRIGHT + "NO transactions to search.")
            return
        
        keyword = input("Enter a keyword to search: ").strip()
        pattern = re.compile(keyword, re.IGNORECASE)
    
        found = False
        for i, t in enumerate(transactions, start=1):
            if (pattern.search(t["type"]) or pattern.search(t["category"])):
                print(f"\nTransaction {i}:")
                print(f"    Type: {t['type']}")
                print(f"    Amount: rup{t['amount']}")
                print(f"    Category: {t['category'].capitalize()}")
                print(f"    Note: {t['note'].capitalize()}")
                print(f"    Date: {t['date']}")
                found = True
    
        if not found:
            print(Fore.RED + Style.BRIGHT + "No matching transactions found.")
    
def export_to_csv():
        transactions = load_transactions()
        if not transactions:
            print(Fore.RED + Style.BRIGHT + "No transactions to export.")
            return
        
        with open("data/transactions.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=transactions[0].keys())
            writer.writeheader()
            writer.writerows(transactions)
        print(Fore.GREEN + "Exported to 'data/transactions.csv'")

def delete_all_json_transactions():
     transactions = load_transactions()
     if not transactions:
          print(Fore.RED + Style.BRIGHT + "No Transactions to delete!")
          return
     
     confirmation = input("Are you sure you want to delete ALL transaction? (yes/no): ").strip().lower()
     if confirmation == "yes":
          with open(DATA_FILE, "w") as file:
               json.dump([], file, indent=4)
               print(Fore.GREEN + "All transaction deleted successfully.")
     else:
               print(Fore.YELLOW + "Delete all cancelled.")

def clear_csv_file(filename):
    with open(filename, "w", newline='') as csvfile:
         pass   
    print(Fore.GREEN + Style.BRIGHT + f"CSV file '{filename} cleared successfully.")
         
               
def main_menu():
    while True:
        print("\n===== Expense Tracker =====")
        print(Fore.YELLOW + "1. AddTransaction")
        print(Fore.YELLOW + "2. View Transactions")
        print(Fore.YELLOW + "3. Delete Transaction")
        print(Fore.YELLOW + "4. view summary")
        print(Fore.YELLOW + "5. search Transactions")
        print(Fore.YELLOW + "6. Export to CSV")
        print(Fore.YELLOW + "7. deletejsonfile")
        print(Fore.YELLOW + "8. clearcsvfile")
        print(Fore.YELLOW + "9. Exit")
        
        choice = input("choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transaction()
        elif choice == "3":
            delete_transaction()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            search_transactions()          
        elif choice == "6":
            export_to_csv()
        elif choice == "7":
            delete_all_json_transactions()
        elif choice == "8":
            clear_csv_file("data/transactions.csv")
        elif choice == "9":
            print(Fore.YELLOW + Style.DIM + "Exiting... Goodbye! ")
            break
        else:
            print("Invalid option. Try again.")

# Run the menu
main_menu()
