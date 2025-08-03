expenses=[]
import datetime
def add_expense():

    amount=float(input("Enter The Amount:₹"))
    category=input("Enter The Category(eg:Food,Travel):")
    description=input("Enter Anything To Note Along...:")
    date=datetime.date.today().isoformat()
    expense={
        "amount":amount,
        "category":category,
        "description":description,
        "date":date
    }
    expenses.append(expense)

def view_expenses():
    if not expenses:
        print("No Expenses Till Now")
        return
    print("\n---All Expenses---")
    for i in expenses:
        print(f"{i['amount']}|{i['category']}|{i['description']}|{i['date']}")
        print()

def filter_by_category():
    if not expenses:
        print("No Expenses To Filter.\n")
        return
    category=input("Enter the category to filter by:").lower()
    flag=False
    print(f"---Expense in Category:{category}---")
    for i in expenses:
        if i["category"].lower()==category:
            print(f"₹{i['amount']}|{i['description']}|{i['date']}")
            flag=True
    if not flag:
        print("No Expenses Found In This Category.")      
        print()  

def total_amount():
    if not expenses:
        print("No Expenses till now...")
        return
    total=0
    for i in expenses:
        total+=i['amount']
        print(f"Total Amount Spent:{total}")

while True:
    print("==Expense Tracker==\n1.Add Expense\n2.View Expenses\n3.Filter By Category\n4.Total Expense Till Now\n5.Exit") 
    choice=input("Choose an option from 1-5 :")
    if choice=="1":
        add_expense()
    elif choice=="2":
        view_expenses()
    elif choice=="3":
        filter_by_category()
    elif choice=="4":
        total_amount()
    elif choice=="5":
        print("GoodBye")   
        break
    else:
        print("Invalid Choice You Fool\n") 

