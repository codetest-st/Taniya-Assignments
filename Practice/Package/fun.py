def sum(n1, n2):
    "Sum of two numbers"
    return n1+n2

print("sum=", sum(20,40))


def fact(n):
    "Factorial of a number"
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print("Factorial=", fact(6))  


def biggest(n1,n2):
    "Returns the biggest number"
    if n1>n2:
     return n1 
    else:
     return n2
print("Biggest=", biggest(20,40))