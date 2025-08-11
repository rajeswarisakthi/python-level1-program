print("Takshashila university")
print("Ongur,tindivanam")
print("-------------------")
print("Student mark list")
print("---------------------")
pymark=int(input("Enter python mark:"))
dbmsmark=int(input("Enter dbms mark:"))
acmark=int(input("Enter accounting mark:"))
total=pymark+dbmsmark+acmark
print("Total mark:",total)
avg=total/3
print("Average mark:",avg)
if pymark>=40 and dbmsmark>=40 and acmark>=40:
    print("Result:pass")
if total>=250:
    print("Grade:o grade*")
elif total>=200:
    print("Grade:a+ grade*")
elif total>=150:
   print("Grade:a grade*")
else:
    print("Grade:b grade*")
    print("Result:fail")
    print("Grade no grade(failed)")
