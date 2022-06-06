import csv
import os.path
from classes.Expenses import Expenses


class DashBoard:
    def __init__(self, user_name):
        self.user_name = user_name
        self.balance = 0
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/dashboard/{self.user_name}.csv")
        file_test = os.path.exists(path)
        if file_test:
            pass
        else:
            with open (path, mode='a', newline='') as csvfile:
                fieldnames = ['monthly_salary']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
            print(f"{user_name}'s dashboard has been initialized.")

    def set_salary(self):
        amount = int(input("Please enter monthly salary amount: "))

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/dashboard/{self.user_name}.csv")

        with open (path, mode='a', newline='') as csvfile:
            fieldnames = ['monthly_salary']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'monthly_salary': amount})
    @staticmethod
    def expense_percent(name, expense_type):
        salary = 0
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/dashboard/{name}.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                salary += int(row['monthly_salary'])
        total_expenses = Expenses.expense_totals(expense_type, name)
        percent = round((total_expenses / salary)*100)
        print(f"The total percent of your monthly salary spent on {expense_type} is {percent}%")

    @staticmethod
    def play_money(name):
        salary = 0
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"../data/dashboard/{name}.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                salary += int(row['monthly_salary'])

        total = Expenses.total_expenses(name)
        play = salary - total
        print(f"{name} your play money for the month is ${play}.")