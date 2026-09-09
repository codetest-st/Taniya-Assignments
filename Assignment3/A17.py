num=int(input("Enter a number:"))
temp= num
sum= 0
while temp > 0:
    digit = temp% 10
    sum= sum * 10 + digit
    temp= temp // 10 
if sum==num:
    print("It's an Armstrong number.")
else:
    print("It's not an Armstrong number.")