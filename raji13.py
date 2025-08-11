print("Rajeswari computer mark")
print("Nehru street,puducherry")
print("-------------------------")
print("Bill recipt")
print("--------------------------")
no=int(input("Enter the item no:"))
name=input("Enter the particular:")
rate=int(input("Enter the quantity:"))
qty=int(input("Enter the quantity:"))
total=rate*qty
print("Total amount in rupes:",total)
if(total>=100000):
   gst=total*10/100
elif(total>=50000):
    gst=total*5/100
elif(total>=20000):
    gst=total*3/100
elif(total>=10000):
    gst=total*2/100
else:
    gst=total*1/100
print("GST(Good &service tax):",gst)
amt=total+gst
print("Amount to be paid:",amt)
    
