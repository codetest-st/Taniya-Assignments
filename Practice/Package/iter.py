def mygenerator():
    print('First item')
    yield 10
    print('Second item')
    yield 40
    print('Last item')
    yield 50


l1=[4,54,66,7,9]
it=iter(l1) 
print(next(it))
print(next(it))
print(next(it))

gen=mygenerator()
print(next(gen))
print(next(gen))
    