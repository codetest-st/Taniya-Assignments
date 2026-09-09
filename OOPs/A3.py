class Quadrilateral:
   def __init__(self,a,b,c,d):
    self.a=a
    self.b=b
    self.c=c
    self.d=d
   def perimeter(self):
      return self.a+self.b+self.c+self.d


   def display(self):
       print("Perimeter:", self.perimeter())

a=int(input("Enter side1:"))
b=int(input("Enter side2:"))
c=int(input("Enter side3:"))
d=int(input("Enter side4:"))

q=Quadrilateral(a,b,c,d)
q.display()