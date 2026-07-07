n1=int(input("Enter first number:"))
i=100
while i<n1:
    if n1%i==0:
        break;
i=i+1
if n1==i:
    print(n1,"is a prime number.")
else:
    print(n1,"is not a prime number.")
