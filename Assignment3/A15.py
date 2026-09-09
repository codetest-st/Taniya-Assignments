num=int(input("Enter a number:"))
temp= num
reverse = 0
while num > 0:
    digit = num % 10
    reverse= reverse * 10 + digit
    num= num // 10 
if temp==reverse:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")