import csv
import os



class Expenses:
    def __init__(self, name, user):
        self.name = name
        self.user = user
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/expenses/{self.user}/{self.name}.csv")
        path2 = os.path.join(my_path, f"../data/expenses/{self.user}/expense_list.csv")
        file_test = os.path.exists(path)
        if file_test:
            pass
        else:
            directory = self.user
            parent_directory = os.path.join(my_path, "../data/expenses/")
            dir_path = os.path.join(parent_directory, directory)
            if os.path.exists(dir_path):
                pass
            else:
                os.mkdir(dir_path)

            with open (path, mode='a', newline='') as csvfile:
                fieldnames = ['item', 'amount']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()

            file_test2 = os.path.exists(path2)
            
            if file_test2:
                with open (path2, mode='a', newline='') as csvfile:
                    fieldnames = ['expense_types']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                    writer.writerow({'expense_types': self.name})
            else:
                with open (path2, mode='a', newline='') as csvfile:
                    fieldnames = ['expense_types']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                    writer.writeheader()
                    writer.writerow({'expense_types': self.name})

    def add_expenses(self, item, amount):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/expenses/{self.user}/{self.name}.csv")

        with open (path, mode='a', newline='') as csvfile:
            fieldnames = ['item', 'amount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'item': item, 'amount': amount})

    @staticmethod
    def total_expenses(user):
        total = 0
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/expenses/{user}/expense_list.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                total += Expenses.expense_totals(row['expense_types'], user)
        return total

    @staticmethod
    def expense_totals(expense_type, user):
        expense_total = 0
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/expenses/{user}/{expense_type}.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                expense_total += int(row['amount'])
        return expense_total

    @staticmethod
    def list_expenses(type, user):
        expense_total = 0
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/expenses/{user}/{type}.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)

            print(f"Your monthly {type} expenses are as follows:")
            for row in reader:
                expense_total += int(row['amount'])
                print(f"{row['item']}: ${row['amount']}")
            print(f"Your total monthly {type} expenses are ${expense_total}")

    @staticmethod
    def remove_expenses(type, user):
        keep_list = []
        remove_value = input("Please type name of expense to be removed: ")
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/expenses/{user}/{type}.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row['item'] == remove_value:
                    pass
                else:
                    keep_list.append(row)
        
        with open (path, mode='w', newline='') as csvfile:
            fieldnames = ['item', 'amount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(keep_list)

    @staticmethod
    def update_expenses(type, user):
        keep_list = []
        update_value = input("Please type name of expense to be updated: ")
        new_amount = int(input("Please enter new expense amount: "))

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/expenses/{user}/{type}.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row['item'] == update_value:
                    row['amount'] = new_amount
                    keep_list.append(row)
                else:
                    keep_list.append(row)
        
        with open (path, mode='w', newline='') as csvfile:
            fieldnames = ['item', 'amount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(keep_list)














