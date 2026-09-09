n1=int(input("Enter marks of English:"))
n2=int(input("Enter marks of Hindi:"))
n3=int(input("Enter marks of Punjabi:"))
n4=int(input("Enter marks of Science:"))
n5=int(input("Enter marks of Maths:"))
total=n1+n2+n3+n4+n5
percentage=total/5
print(f"The total marks of 5 subjects is {total}")
print(f"The  percentage of 5 subjects is {percentage}")

if percentage >= 95:
   print ("First Division")
elif percentage >= 80:
     print("Second Division")
elif percentage >= 70:
     print("Third Division") 
elif percentage >= 90:
     print("Merit") 
else:
     print("Fail")