def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

num=8
f=factorial(num)
print(f"Factorial of {num} is {f}")