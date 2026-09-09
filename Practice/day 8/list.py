x=[2,5,7,6,4,10]
y=[i**2 for i in x]
data=[f"{i} even" if i%2==0 else f"{i} odd" for i in x]
print(data)