sp=int(input("Enter sale price of a product:"))
cp=int(input("Enter cost price of a product:"))
if sp > cp:
    profit=sp - cp
    print(f"The profit is {profit} ")
else:
    loss= cp - sp
    print(f"The loss is {loss}")