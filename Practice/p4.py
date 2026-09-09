def fun(num):
    num=10
    print(f"The address of Num: {num} is {id(num)}")
x=100
fun(x)
print(f"The address of X: {x} is {id(x)}")