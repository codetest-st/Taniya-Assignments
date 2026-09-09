def isprime(num):
    i=1
    while i<num:
        if num%i==0:
            break
        i+=1
    if num==i:
        return True
    else:
       return False

l1=[22,45,65,7,2,34]
l2=list(filter(isprime,l1))

print(12)