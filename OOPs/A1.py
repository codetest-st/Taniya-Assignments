class Box:
   def __init__(self,l,b,h):
    self.l=l
    self.b=b
    self.h=h
       
   def vol(self):
      return self.l*self.b*self.h
   
   def area(self):
     return self.l*self.b

   def display(self):
       print("volume:", self.vol())
       print("Area:", self.area())

l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
h=int(input("Enter height:"))

b1=Box(l,b,h)
b1.display()