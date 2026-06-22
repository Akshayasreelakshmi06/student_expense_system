students=[]
for i in range(3):
    name=input("Enter student name:")
    marks=[]
    for j in range(3):
        mark=int(input("Enter the marks:"))
        marks.append(mark)
    total=sum(marks)
    avg=sum(marks)/len(marks)
    if avg>=50:
        result="pass"
    else:
        result="fail"
    student={
        "name":name,
        "marks":marks,
        "total":total,
        "avg":avg,
        "result":result
        }
    students.append(student)
expenses=[]
for i in range(3):
    expense_name=input("Enter the expense name:")
    amount=int(input("Enter the amount:"))
    expense={
        "expense_name":expense_name,
        "amount":amount
        }
expenses.append(expense)
total_expense=0
max_expense=expenses[0]
min_expense=expenses[0]
for e in expenses:
    total_expense+=e["amount"]
    if e["amount"]>max_expense["amount"]:
        max_expense=e
    if e["amount"]<min_expense["amount"]:
        min_expense=e
               
print("\n----STUDENT REPORT----")
for s in students:
               print(s["name"],s["marks"],s["total"],s["avg"],s["result"])
print("\n----EXPENSE REPORT----")
for e in expenses:
               print(e["expense_name"],e["amount"])
print("\nTotal Expense:",total_expense)
print("\nHighest expense:",max_expense["expense_name"],max_expense["amount"])
print("\nLowest expense:",min_expense["expense_name"],min_expense["amount"])
