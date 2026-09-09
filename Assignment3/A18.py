num=int(input("Enter a number:"))
binary=" "
if num==0:
    print("Binary = 0")
else:
    while num > 0:
        rem = num % 2
        binary = str(rem)+binary
        num= num // 2
    print("Binary =", binary)