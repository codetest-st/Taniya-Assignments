def display(lst):
    print(f"List: {lst} and Address of list: {id(numbers)}")
    lst.append(10)
    print(f"List after modification: {lst} and Address of list: {id(lst)}")


numbers=[1,2,3,4,5]
print(f"List before fumction call: {numbers} and Address of list is: {id(numbers)}")
display (numbers)
print(f"List after function call: {numbers} and Address of list:{id(numbers)}")