print("Nivedha international[p]ltd")
print("NO.15,Nagapuram dist,bangalore")
print("------------------------------")
print("Employee payroll system")
print("-------------------------------")
Id=int(input("Enter the employeeid:"))
name=input("Enter the name:")
salary=int(input("Enter the salary:"))
print("Income")
Bonas=salary*20/100
print("Bonas(20 per):",Bonas)
overtime=salary*10/100
print("overtime(10 per):",overtime)
travel=salary*5/100
print("Travel allowance(5 per):",travel)
gross=salary+Bonas+overtime+travel
print("Grosspay in ruppess:",gross)
