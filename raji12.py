print("Government of tamilnadu")
print("Electricity board")
print("-------------------------")
print("Bill recipt")
print("---------------------------")
eb=int(input("Enter the eb.no:,"))
cn=input("Enter the customer name:,")
pu=int(input("Enter the previous unit:,"))
cu=int(input("Enter the current unit:,"))
unit=pu+cu
print("Unit consumed:",unit)
if(unit>=1000):
    amt=unit*10
    print("Amount to be paid:",amt)
elif(unit>=500):
    amt=unit*5
    print("Amount to be paid:",amt)
elif(unit>=100):
    amt=unit*2
    print("Amount to be paid:",amt)
else:
    print("Amount to be paid:",nill)
