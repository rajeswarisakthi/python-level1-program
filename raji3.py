print("Nivedha Supermarket")
print("No.44,nehrustreet,puducherry")
print("----------------------------")
print("Bill receipt")
print("-----------------------------")
no=int(input("Enter the serial number:"))
str=input("Enter the particular:")
no1=int(input("Enter the quaulity:"))
no2=int(input("Enter the rate:"))
Total=no1*no2
print("Total amount rs:",Total)
GST=Total*10/100
print("GST(10per):",GST)
paid=Total+GST
print("Amount to be paid:",paid)
