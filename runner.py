from classes.CheckBook import CheckBook
from classes.Expenses import Expenses
from classes.DashBoard import DashBoard

user = (input("Please enter the user name: ")).lower()

prompt = (f"""What would you like to do {user}?
Options:
1. Check balance.
2. Add transaction to check book.
3. Display recent transactions.
4. List expenses for a set <category>
5. Remove an expense.
6. Update expense amount.
7. Check percentage of income spent on expense category. 
8. Play money amount after monthly recurring expenses. 
9. Set monthly income. 
10. initialize a new user. 
Q. Quit
: """)

mode = input(prompt)

while mode != 'Q':
    if mode == '1':
        CheckBook.current_balance(user)
        mode = input(prompt)
    elif mode == '2':
        CheckBook.add_transaction(user)
        mode = input(prompt)
    elif mode == '3':
        CheckBook.recent_activity(user)
        mode = input(prompt)
    elif mode == '4':
        type = (input("Please enter the expense category <type>: ")).lower()
        Expenses.list_expenses(type, user)
        mode = input(prompt)
    elif mode == '5':
        type = (input("Please enter the expense category <type>: ")).lower()
        Expenses.remove_expenses(type, user)
        mode = input(prompt)
    elif mode == '6':
        type = (input("Please enter the expense category <type>: ")).lower()
        Expenses.update_expenses(type, user)
        mode = input(prompt)
    elif mode == '7':
        type = (input("Please enter the expense category <type>: ")).lower()
        DashBoard.expense_percent(user, type)
        mode = input(prompt)
    elif mode == '8':
        DashBoard.play_money(user)
        mode = input(prompt)
    elif mode == '9':
        dash_user = user
        dash_user = DashBoard(user)
        dash_user.set_salary()
        mode = input(prompt)
    elif mode == '10':
        new_user = (input("Please enter the user name: ")).lower()
        new_user = CheckBook(new_user) 
        mode = input(prompt)
    else:
        pass
