hrs=int(input("Enter working hours:"))
if hrs==8:
    wage=250
    print("Wage = Rs.",wage)
elif hrs > 8 and hrs <=10:
    wage= 250+(hrs-8)*50
    print("Wage= Rs.",wage)
elif hrs > 10 and hrs <=12:
    wage= 250+(2*50)+(hrs-10)*75
    print("Wage= Rs.",wage)
elif hrs > 12 and hrs <=14:
    wage= 250+(2*50)+(2*75)+(hrs-12)*100
    print("Wage= Rs.", wage)
else:
    print("Invalid working hour")


