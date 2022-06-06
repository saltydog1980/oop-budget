import csv
import os.path
from classes.DashBoard import DashBoard
from classes.Expenses import Expenses

class CheckBook(DashBoard):
    def __init__(self, user_name):
        self.user_name = user_name
        self.balance = 0
        self.dash_init = user_name
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/checkbook/{self.user_name}.csv")
        file_test = os.path.exists(path)
        if file_test:
            pass
        else:
            self.dash_init = DashBoard(user_name)
            with open (path, mode='a', newline='') as csvfile:
                fieldnames = ['item', 'type', 'amount']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
        print(f"{user_name}'s check book has been created.")
    
    @staticmethod
    def add_transaction(user):
        item = input("Please enter the name of the transaction to add: ")
        type = input("Please enter the type of transaction to add: ")
        amount = int(input("Please enter amount: "))

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/checkbook/{user}.csv")

        with open (path, mode='a', newline='') as csvfile:
            fieldnames = ['item', 'type', 'amount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'item': item, 'type': type, 'amount': amount})
        if type != 'deposit':
            type = Expenses(type, user)
            type.add_expenses(item, amount)

    @staticmethod
    def recent_activity(self):
        current_balance = 0
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/checkbook/{self}.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)

            print(f"{self}'s recent transactions are as follows:")
            for row in reader:
                
                if row['type'] == 'deposit':
                    current_balance += int(row['amount'])
                    print(f"{row['item']} + ${row['amount']}")
                else:
                    current_balance -= int(row['amount'])
                    print(f"{row['item']} - ${row['amount']}")
                
            print(f"Your current balance is: ${current_balance}")

    @staticmethod
    def current_balance(self):
        current_balance = 0
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/checkbook/{self}.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                
                if row['type'] == 'deposit':
                    current_balance += int(row['amount'])
                else:
                    current_balance -= int(row['amount'])
                
            print(f"{self}'s current balance is: ${current_balance}")
