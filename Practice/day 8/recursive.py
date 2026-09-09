def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    #5*24
    #4*6
    #3*2
    #2*1
x=fact(5) #120
print(x)